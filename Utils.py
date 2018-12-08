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

SPAWN_TIMES = { # From here onwards can be changed freely
    'spike' : 50,
    'food' : 50,
    'worm' : 10000}
EPS = 0.1 # decision threshold (if worm decides in -EPS < decision < EPS, he does not perform any action), this affects even crazy actions
FOOD_RESTORATION = 10
SPIKE_DAMAGE = 10
WORM_DAMAGE = 5
WORM_MEMORY_SIZE = 100
INITIAL_LR = 0.001
LEARN_BATCH_SIZE = 5
HEALTH_COEF = 0.5
SATURATION_COEF = 0.5
AGE_ACTIVITY = 10
RENDER_DELAY = 50 # ms

cmd_params = {
    'worms-init-num=' : 'Initial number of worms (int)',
    'food-init-num=' : 'Initial number of food (int)',
    'spike-init-num=' : 'Initial number of spikes (int)',
    'world-width=' : 'Width of the world (int)',
    'world-height=' : 'Height of the world (int)',
    'learning' : 'Learning',
    'world-lifespan=' : 'Lifespan of the world (int)',
    'spike-lifespan=' : 'Lifespan of spike (int)',
    'food-lifespan=' : 'Lifespan of food (int)',
    'worm-lifespan=' : 'Lifespan of the worm (int)',
    'worm-speed=' : 'Speed of worm (int)',
    'worm-adequacy=' : 'Adequacy of worm (chance to do as worm decided) (float, from 0 to 1)',
    'adequacy-increase-span=' : 'Period of worm lifespan within which the worm gets completely adequate (float, from 0 to 1)',
    'learn-frequency=' : 'Frequency of learning sessions (less than worm lifespan, more than 0) (int)',
    'visual-width-scale=' : 'Scale of visual width (int)',
    'visual-height-scale=' : 'Scale of visual height (int)',
    'visual-debug-show' : 'Do debug visual',
    'visual-save-recap' : 'Do save video recap',
    'visual-fps=' : 'FPS rate in video recap (int)'}

cmd_to_thread = {
    'worms-init-num' : 'worms_init_number',
    'food-init-num' : 'food_init_number',
    'spike-init-num' : 'spike_init_number',
    'world-width' : 'world_width',
    'world-height' : 'world_height',
    'learning' : 'learning',
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

thread_params = {
    'worms_init_number' : 1,
    'food_init_number' : 1,
    'spike_init_number' : 1,
    'world_width' : 100,
    'world_height' : 100,
    'learning' : False,
    'world_lifespan' : 10000,
    'spike_lifespan' : 100,
    'food_lifespan' : 100,
    'worm_lifespan' : 100,
    'worm_speed' : 5,
    'worm_adequacy' : 0.8,
    'adequacy_increase_span' : 0.5,
    'learn_freq' : 10,
    'visual_width_scale' : 2,
    'visual_height_scale' : 2,
    'visual_debug_show' : False,
    'visual_save_recap' : False,
    'visual_worm_draw_color' : (255, 0, 0),
    'visual_spike_draw_color' : (0, 0, 255),
    'visual_food_draw_color' : (0, 255, 0),
    'visual_fps' : 5}
