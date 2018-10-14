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
EPS = 0.15
FOOD_RESTORATION = 10
SPIKE_DAMAGE = 10
WORM_DAMAGE = 5
RENDER_DELAY = 1000 # ms

cmd_params = {
    'worms-init-num=' : 'Initial number of worms',
    'food-init-num=' : 'Initial number of food',
    'spike-init-num=' : 'Initial number of spikes',
    'world-width=' : 'Width of the world',
    'world-height=' : 'Height of the world',
    'learning=' : 'Learning',
    'world-lifespan=' : 'Lifespan of the world',
    'spike-lifespan=' : 'Lifespan of spike',
    'food-lifespan=' : 'Lifespan of food',
    'worm-lifespan=' : 'Lifespan of the worm'}

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
    'worm-lifespan' : 'worm_lifespan'}

thread_params = {
    'worms_init_number' : 1,
    'food_init_number' : 1,
    'spike_init_number' : 1,
    'world_width' : 100,
    'world_height' : 100,
    'learning' : False,
    'world_lifespan' : 10000,
    'spike_lifespan' : 10,
    'food_lifespan' : 10,
    'worm_lifespan' : 100}
