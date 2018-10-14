import sys, getopt
import numpy as np
import numpy.random as npr
from time import sleep

from Food import *
from Spike import *
from Environment import *

from Worm import *
from Colony import *

from Utils import *

class Thread:
    def __init__(self, params):
        self.params = params
        self.params.update({'tick' : 0})
        
        env_max_times = {'spike' : params['spike_lifespan'], 'food' : params['food_lifespan']}
        self.environment = Environment(env_max_times)
        
        self.colony = Colony(params['worm_lifespan'])
    
    def _generate_init_worms(self):
        worms_params_x = npr.randint(0, self.params['world_width'], self.params['worms_init_number'])
        worms_params_y = npr.randint(0, self.params['world_height'], self.params['worms_init_number'])
        worms_params_orient = npr.randint(0, 4, self.params['worms_init_number'])
        for _ in range(self.params['worms_init_number']):
            x = worms_params_x[_]
            y = worms_params_y[_]
            orient = worms_params_orient[_]
            self.colony.emplace_worm(x, y, orient)
    
    def _generate_init_spikes(self):
        spike_params_x = npr.randint(0, self.params['world_width'], self.params['spike_init_number'])
        spike_params_y = npr.randint(0, self.params['world_height'], self.params['spike_init_number'])
        for _ in range(self.params['spike_init_number']):
            x = spike_params_x[_]
            y = spike_params_y[_]
            self.environment.emplace_spike(x, y)
    
    def _generate_init_food(self):
        food_params_x = npr.randint(0, self.params['world_width'], self.params['food_init_number'])
        food_params_y = npr.randint(0, self.params['world_height'], self.params['food_init_number'])
        for _ in range(self.params['food_init_number']):
            x = food_params_x[_]
            y = food_params_y[_]
            self.environment.emplace_food(x, y)

    def _tick(self):
        self.params['tick'] += 1
        self.environment.tick()
        self.colony.tick()
    
    def _is_alive(self):
        if self.params['tick'] <= self.params['world_lifespan']:
            return True
        else:
            return False
    
    def _render_world(self):
        world = np.zeros((self.params['world_width'], self.params['world_height'], 3), dtype=float)
        for x in range(self.params['world_width']):
            for y in range(self.params['world_height']):
                env_interception = self.environment.interception(x, y)
                colony_interception = self.colony.interception(x, y)
                world[x, y, 0] = colony_interception
                world[x, y, 1] = env_interception[0]
                world[x, y, 2] = env_interception[1]
        return world
    
    def _get_worm_view(self, worm_position):
        worm_x = worm_position[0]
        worm_y = worm_position[1]
        worm_orient = worm_position[2]
        vb = {
            'x1' : worm_x,
            'x2' : worm_x,
            'y1' : worm_y,
            'y2' : worm_y
        }
        if worm_orient == ORIENTATIONS['top']:
            vb['x1'] -= VIEW['left']
            vb['x2'] += VIEW['right'] + 1
            vb['y1'] -= VIEW['forward'] + WORM_LENGTH
            vb['y2'] += VIEW['backward']
        elif worm_orient == ORIENTATIONS['bottom']:
            vb['x1'] -= VIEW['right'] + 1
            vb['x2'] += VIEW['left']
            vb['y1'] -= VIEW['backward']
            vb['y2'] += VIEW['forward'] + WORM_LENGTH
        elif worm_orient == ORIENTATIONS['left']:
            vb['x1'] -= VIEW['forward'] + WORM_LENGTH
            vb['x2'] += VIEW['backward']
            vb['y1'] -= VIEW['right'] + 1
            vb['y2'] += VIEW['left']
        elif worm_orient == ORIENTATIONS['right']:
            vb['x1'] -= VIEW['backward']
            vb['x2'] += VIEW['forward'] + WORM_LENGTH
            vb['y1'] -= VIEW['left']
            vb['y2'] += VIEW['right'] + 1
        else:
            return None
        return vb
    
    def _rotate_worm_view(self, worm_view, orientation):
        if orientation > 0:
            for i in range(orientation):
                worm_view = np.rot90(worm_view)
    
    def _update_worm_position(self, position, action):
        turn = action[0]
        move = action[1]
        if turn > EPS: # turn left
            position[2] -= 1
            position[2] %= 4
        elif turn < EPS: # turn right
            position[2] += 1
            position[2] %= 4
        move_value = 0
        if move > EPS: # move forward
            move_value = 1
        elif move < EPS: # move backward
            move_value = -1
        # actual moving
        if position[2] == ORIENTATIONS['top']:
            position[1] -= move_value
            position[1] %= self.params['world_height']
        elif position[2] == ORIENTATIONS['bottom']:
            position[1] += move_value
            position[1] %= self.params['world_height']
        elif position[2] == ORIENTATIONS['left']:
            position[0] -= move_value
            position[1] %= self.params['world_width']
        elif position[2] == ORIENTATIONS['right']:
            position[0] += move_value
            position[1] %= self.params['world_width']
        return position
    
    def _colony_interaction(self, worm, attack):
        worm_position = worm.get_position()
        worm_x, worm_y = worm_position[0], worm_position[1]
        int_worm = None
        if self.world_view[worm_x, worm_y, 0] > 0:
            # TODO: Interaction with tails (they live on sphere)
            int_worm = self.colony.get_worm_by_position(worm_x, worm_y)
        if int_worm:
            if attack > EPS: # if worm decided to attack
                old_health = int_worm.get_health()
                new_health = old_health - WORM_DAMAGE
                int_worm.set_health(new_health)
    
    def _food_interaction(self, worm, attack):
        worm_position = worm.get_position()
        worm_x, worm_y = worm_position[0], worm_position[1]
        int_food = None
        if self.world_view[worm_x, worm_y, 2] > 0:
            int_food = self.environment.get_food_by_position(worm_x, worm_y)
        if int_food:
            restore = int_food.eat()
            old_health = worm.get_health()
            new_health = old_health + restore
            worm.set_health(new_health)
            if attack > EPS: # if worm decided to attack
                int_food.eat() # food gets double hit
        
    def _spike_interaction(self, worm, attach):
        worm_position = worm.get_position()
        worm_x, worm_y = worm_position[0], worm_position[1]
        int_spike = None
        if self.world_view[worm_x, worm_y, 1] > 0:
            int_spike = self.environment.get_spike_by_position(worm_x, worm_y)
        if int_spike:
            int_spike.hit()
            old_health = worm.get_health()
            new_health = old_health - SPIKE_DAMAGE
            worm.set_health(new_health)
            if attack > EPS: # if worm decided to attack
                int_spike.hit() # spike gets double hit
    
    def _environment_interaction(self, worm, attack):
        self._spike_interaction(worm, attack)
        self._food_interaction(worm, attack)
    
    def _spawn_spike(self):
        if self.params['tick'] % SPAWN_TIMES['spike'] == 0:
            x_pos = npr.randint(0, self.params['world_width'])
            y_pos = npr.randint(0, self.params['world_height'])
            self.environment.emplace_spike(x, y)
    
    def _spawn_food(self):
        if self.params['tick'] % SPAWN_TIMES['food'] == 0:
            x_pos = npr.randint(0, self.params['world_width'])
            y_pos = npr.randint(0, self.params['world_height'])
            self.environment.emplace_food(x, y)
    
    def _spawn_worm(self):
        if self.params['tick'] % SPAWN_TIMES['worm'] == 0:
            x_pos = npr.randint(0, self.params['world_width'])
            y_pos = npr.randint(0, self.params['world_height'])
            orient = npr.randint(0, 4)
            self.colony.emplace_worm(x, y, orient)
    
    def _spawn(self):
        self._spawn_spike()
        self._spawn_food()
        self._spawn_worm()
    
    def _run(self):
        while(self._is_alive()):
            self._tick()
            self.world_view = self._render_world()
            for worm in self.colony:
                worm_position = list(worm.get_position())
                print("Worm %d, position (%d, %d)" % (worm.get_id(), worm_position[0], worm_position[1]))
                vb = self._get_worm_view(worm_position)
                # TODO: view through the edge
                worm_view = self.world_view[vb['x1'] : vb['x2'], vb['y1'] : vb['y2'], :].copy()
                self._rotate_worm_view(worm_view, worm_position[2])
                action = worm(worm_view) # feed worm view to worm
                attack = action[2]
                self._update_worm_position(worm_position, action)
                worm.set_position(*worm_position)
                self._colony_interaction(worm, attack)
                self._environment_interaction(worm, attack)
            self.colony.clean_up()
            self.environment.clean_up()
            self._spawn()
            sleep(RENDER_DELAY*(10**(-3)))

    def generate(self):
        self._generate_init_worms()
        self._generate_init_spikes()
        self._generate_init_food()
    
    def start(self):
        self._run()


if __name__ == "__main__":
    opts, _ = getopt.getopt(sys.argv[1:], "", cmd_params.keys())
    for key, value in opts:
        if key[2:] in cmd_to_thread.keys():
            param_name = cmd_to_thread[key[2:]]
            thread_params[param_name] = int(value)
            print('-< %s has been set to %s\n' % (cmd_params[key[2:] + "="], str(value)))
    main = Thread(thread_params)
    main.generate()
    main.start()

