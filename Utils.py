WORM_LENGTH = 2 #     <-- INTERNAL PARAMETERS!
ORIENTATIONS = { #    < DO NOT TOUCH FROM THIS
    'top' : 0, #      <
    'right' : 1, #    <
    'bottom' : 2, #   <
    'left' : 3} #     <
VIEW = { #            <
    'forward' : 5, #  <
    'backward' : 5, # <
    'left' : 5, #     <
    'right' : 5} #    <-- TO THIS

WORM_MEMORY_SIZE = 100 # <-- LEARNING PARAMETERS!
INITIAL_LR = 0.001 #     <   Initial learning rate, try different values
LEARN_BATCH_SIZE = 5 #   <   We learn on random batch from worm memory, this is max batch size
HEALTH_COEF = 0.5 #      <   REWARD FORMULA IS:
SATURATION_COEF = 0.5 #  <   reward = HEALTH_COEF*delta_health + SATURATION_COEF*delta_saturation
AGE_ACTIVITY = 10 #      <-- lr = (INITIAL_LR  - reward/float(100))*float(AGE_ACTIVITY)/(1 + (self.time**2))

# HYPERPARAMETERS
# From here onwards can be changed freely
EPS = 0.1 # decision threshold (if worm decides in -EPS < decision < EPS, he does not perform any action), this affects even crazy actions
FOOD_RESTORATION = 10 # Food restores Health
SPIKE_DAMAGE = 10 # Spike reduces health
SPIKE_DAMAGE_AOE = 2 # Spike hits in aoe (l1 metrics)
WORM_DAMAGE = 5 # Worm reduces other worm health if attacks
RENDER_DELAY = 50 # Render delay when visual debug show ms

# DEFAULT PARAMS MANIPULATION
thread_params = { # You can set the params here directly
    'worms_init_number' : 1,
    'food_init_number' : 1,
    'spike_init_number' : 1,
    'spike_spawn_time' : 50,
    'food_spawn_time' : 50,
    'worm_spawn_time' : 10000,
    'spike_spawn_amount' : 1,
    'food_spawn_amount' : 1,
    'worm_spawn_amount' : 1,
    'world_width' : 100,
    'world_height' : 100,
    'learning' : False,
    'breeding' : False,
    'breeding_age' : 10,
    'world_lifespan' : 10000,
    'spike_lifespan' : 100,
    'food_lifespan' : 100,
    'worm_lifespan' : 100,
    'worm_speed' : 5,
    'worm_adequacy' : 0.8,
    'adequacy_increase_span' : 0.5,
    'learn_freq' : 10,
    'visual_width_scale' : 8,
    'visual_height_scale' : 8,
    'visual_debug_show' : False,
    'visual_save_recap' : False,
    'visual_worm_draw_color' : (255, 0, 0),
    'visual_spike_draw_color' : (0, 0, 255),
    'visual_food_draw_color' : (0, 255, 0),
    'visual_fps' : 5}

# DESCRIPTION TABLE
cmd_params = { # Or you can start Thread.py with parameters from this list, the second string is the description (all flags start with --)
    'worms-init-num=' : 'Initial amount of worms (int)',
    'food-init-num=' : 'Initial amount of food (int)',
    'spike-init-num=' : 'Initial amount of spikes (int)',
    'spike-spawn-time=' : 'Time for spawn new spikes (int)',
    'food-spawn-time=' : 'Time for spawn new food (int)',
    'worm-spawn-time=' : 'Time for spawn new worms (int)',
    'spike-spawn-amount=' : 'Amount of new spikes to be spawned (int)',
    'food-spawn-amount=' : 'Amount of new food to be spawned (int)',
    'worm-spawn-amount=' : 'Amount of new worms to be spawned (int)',
    'world-width=' : 'Width of the world (int)',
    'world-height=' : 'Height of the world (int)',
    'learning' : 'Learning',
    'breeding' : 'Breeding',
    'breeding-age=' : 'Breeding age (int)',
    'world-lifespan=' : 'Lifespan of the world (int)',
    'spike-lifespan=' : 'Lifespan of spike (int)',
    'food-lifespan=' : 'Lifespan of food (int)',
    'worm-lifespan=' : 'Lifespan of the worm (int)',
    'worm-speed=' : 'Speed of worm (int)',
    'worm-adequacy=' : 'Adequacy of worm (chance to do as worm decided) (float, from 0 to 1)',
    'adequacy-increase-span=' : 'Period of worm lifespan within which the worm gets completely adequate (float, from 0 to 1)',
    'learn-frequency=' : 'Frequency of learning sessions (less than worm lifespan, more than LEARN_BATCH_SIZE) (int)',
    'visual-width-scale=' : 'Scale of visual width (int)',
    'visual-height-scale=' : 'Scale of visual height (int)',
    'visual-debug-show' : 'Do debug visual',
    'visual-save-recap' : 'Do save video recap',
    'visual-fps=' : 'FPS rate in video recap (int)'}

cmd_to_thread = { # INTERNAL USAGE ONLY
    'worms-init-num' : 'worms_init_number',
    'food-init-num' : 'food_init_number',
    'spike-init-num' : 'spike_init_number',
    'spike-spawn-time' : 'spike_spawn_time',
    'food-spawn-time' : 'food_spawn_time',
    'worm-spawn-time' : 'worm_spawn_time',
    'spike-spawn-amount' : 'spike_spawn_amount',
    'food-spawn-amount' : 'food_spawn_amount',
    'worm-spawn-amount' : 'worm_spawn_amount',
    'world-width' : 'world_width',
    'world-height' : 'world_height',
    'learning' : 'learning',
    'breeding' : 'breeding',
    'breeding-age' : 'breeding_age',
    'world-lifespan' : 'world_lifespan',
    'spike-lifespan' : 'spike_lifespan',
    'food-lifespan' : 'food_lifespan',
    'worm-lifespan' : 'worm_lifespan',
    'worm-speed' : 'worm_speed',
    'worm-adequacy' : 'worm_adequacy',
    'adequacy-increase-span' : 'adequacy_increase_span',
    'learn-frequency' : 'learn_freq',
    'visual-width-scale' : 'visual_width_scale',
    'visual-height-scale' : 'visual_height_scale',
    'visual-debug-show' : 'visual_debug_show',
    'visual-save-recap' : 'visual_save_recap',
    'visual-fps' : 'visual_fps'}
