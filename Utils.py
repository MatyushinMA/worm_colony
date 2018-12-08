WORM_LENGTH = 2
ORIENTATIONS = {
    'top' : 0,
    'right' : 1,
    'bottom' : 2,
    'left' : 3}
VIEW = {
    'forward' : 5,
    'backward' : 5,
    'left' : 5,
    'right' : 5}
SPAWN_TIMES = {
    'spike' : 50,
    'food' : 50,
    'worm' : 10000}
EPS = 0.0
FOOD_RESTORATION = 10
SPIKE_DAMAGE = 10
WORM_DAMAGE = 5
RENDER_DELAY = 50 # ms

cmd_params = {
    'worms-init-num=' : 'Initial number of worms',
    'food-init-num=' : 'Initial number of food',
    'spike-init-num=' : 'Initial number of spikes',
    'world-width=' : 'Width of the world',
    'world-height=' : 'Height of the world',
    'learning' : 'Learning',
    'world-lifespan=' : 'Lifespan of the world',
    'spike-lifespan=' : 'Lifespan of spike',
    'food-lifespan=' : 'Lifespan of food',
    'worm-lifespan=' : 'Lifespan of the worm',
    'worm-speed=' : 'Speed of worm',
    'worm-adequacy=' : 'Adequacy of worm (chance to do as worm decided)',
    'adequacy-increase-span=' : 'Period of worm lifespan within which the worm gets completely adequate',
    'visual-width-scale=' : 'Scale of visual width',
    'visual-height-scale=' : 'Scale of visual height',
    'visual-debug-show=' : 'Do debug visual',
    'visual-save-recap=' : 'Do save video recap'}

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
    'visual-width-scale' : 'visual_width_scale',
    'visual-height-scale' : 'visual_height_scale',
    'visual-debug-show' : 'visual_debug_show',
    'visual-save-recap' : 'visual_save_recap'}

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
    'visual_width_scale' : 2,
    'visual_height_scale' : 2,
    'visual_debug_show' : 0,
    'visual_save_recap' : 0,
    'visual_worm_draw_color' : (255, 0, 0),
    'visual_spike_draw_color' : (0, 0, 255),
    'visual_food_draw_color' : (0, 255, 0),
    'visual_fps' : 5}
