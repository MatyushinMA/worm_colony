from Nnet import WormNET
from Memory import Storage
from Utils import WORM_MEMORY_SIZE, INITIAL_LR, LEARN_BATCH_SIZE
from Utils import HEALTH_COEF, SATURATION_COEF, EPS, AGE_ACTIVITY
from Utils import SATURATION_TICK_REDUCTION, STARVATION_DAMAGE_THRESHOLD
from Utils import STARVATION_DAMAGE, SATURATION_HEAL_THRESHOLD, SATURATION_HEAL
from Utils import BREEDING_COEF
from math import fabs

import torch
import torch.nn as nn
import numpy.random as npr

class Worm:
    def __init__(self, id, x, y, orientation=0, weights=None):
        self.id = id
        self.health = 100.
        self.time = 0
        self.power = 1
        self.saturation = 100.
        self.orient = orientation
        self.bred = False

        self.net = WormNET()
        if weights:
            self.net.load_state_dict(weights)
        self.storage = Storage(WORM_MEMORY_SIZE)
        self.optimizer = torch.optim.Adam(self.net.parameters(), INITIAL_LR)
        self.loss_fn = nn.CrossEntropyLoss()
        self.x = x
        self.y = y

    def __call__(self, env):
        feed_env = torch.from_numpy(env.copy())
        feed_env = feed_env.permute(2, 0, 1)
        feed_env = feed_env.view(1, 3, 11, 12)
        feed_env = feed_env.float()
        self._view = feed_env
        with torch.no_grad():
            probs, pred = self.net(feed_env)
        self._act = pred
        self._state = {
            'health' : self.health,
            'saturation' : self.saturation
        }
        return pred

    def memorize(self):
        if self.time > 0:
            self._state['health'] = self.health - self._state['health']
            self._state['saturation'] = self.saturation - self._state['saturation']
            self.storage.push_memo(self._view, self._act, self._state)

    def learn(self, global_tick):
        if self.time == 0:
            return
        self.net.train()
        lbs = npr.randint(1, LEARN_BATCH_SIZE)
        learn_batch = self.storage.batch(lbs)
        for view, act, state in learn_batch:
            reward = HEALTH_COEF*state['health'] + SATURATION_COEF*state['saturation'] + BREEDING_COEF*int(self.bred)
            if reward <= 0:
                target = [torch.zeros([1, 1, 1], dtype=torch.long), torch.zeros([1, 1, 1], dtype=torch.long), torch.zeros([1, 1, 1], dtype=torch.long)]
                for act_id in range(3):
                    if act[act_id] > EPS:
                        target[act_id][0] = 1
                    elif act[act_id] >= -EPS: # Stagnation penalty
                        target[act_id][0] = npr.randint(0, 2)
                lr = (INITIAL_LR  - reward/float(100))*float(AGE_ACTIVITY)/((self.time)*global_tick)
                for param_group in self.optimizer.param_groups:
                    param_group['lr'] = lr

                prob, _ = self.net(view)
                loss1 = self.loss_fn(prob[0], target[0])
                loss2 = self.loss_fn(prob[1], target[1])
                loss3 = self.loss_fn(prob[2], target[2])
                loss = loss1 + loss2 + loss3

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
            else:
                target = [torch.ones([1, 1, 1], dtype=torch.long), torch.ones([1, 1, 1], dtype=torch.long), torch.ones([1, 1, 1], dtype=torch.long)]
                for act_id in range(3):
                    if act[act_id] > EPS:
                        target[act_id][0] = 0
                    elif act[act_id] >= -EPS: # Stagnation encouraging
                        target[act_id][0] = -1
                lr = max(INITIAL_LR  - reward/float(100), 0.)*float(AGE_ACTIVITY)/((self.time)*global_tick)
                for param_group in self.optimizer.param_groups:
                    param_group['lr'] = lr

                prob, _ = self.net(view)
                loss1 = None
                flag1 = False
                loss2 = None
                flag2 = False
                loss3 = None
                flag3 = False
                if target[0].item() >= 0:
                    loss1 = self.loss_fn(prob[0], target[0])
                    flag1 = True
                if target[1].item() >= 0:
                    loss2 = self.loss_fn(prob[1], target[1])
                    flag2 = True
                if target[2].item() >= 0:
                    loss3 = self.loss_fn(prob[2], target[2])
                    flag3 = True

                self.optimizer.zero_grad()
                if flag1:
                    loss = loss1
                    if flag2:
                        loss += loss2
                    if flag3:
                        loss += loss3
                    loss.backward()
                    self.optimizer.step()
                elif flag2:
                    loss = loss2
                    if flag3:
                        loss += loss3
                    loss.backward()
                    self.optimizer.step()
                elif flag3:
                    loss = loss3
                    loss.backward()
                    self.optimizer.step()

    def get_id(self):
        return self.id

    def get_power(self):
        return self.power

    def set_power(self, p):
        self.power = p

    def get_health(self):
        return self.health

    def set_health(self, h):
        self.health = h
        self.health = max(min(self.health, 100), 0)

    def get_saturation(self):
        return self.saturation

    def set_saturation(self, s):
        self.saturation = s

    def get_time(self):
        return self.time

    def tick(self):
        self.time += 1
        self.bred = False

    def restore(self):
        self.saturation -= SATURATION_TICK_REDUCTION
        self.saturation = max(self.saturation, 0.)
        if self.saturation <= STARVATION_DAMAGE_THRESHOLD:
            self.health -= STARVATION_DAMAGE
            self.health = max(self.health, 0.)
        elif self.saturation >= SATURATION_HEAL_THRESHOLD:
            self.health += SATURATION_HEAL
            self.health = min(self.health, 100.)

    def breed_restore(self):
        self.bred = True

    def did_bred(self):
        return self.bred

    def get_position(self):
        return (self.x, self.y, self.orient)

    def set_position(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orient = orientation

    def get_state_dict(self):
        return self.net.state_dict()
