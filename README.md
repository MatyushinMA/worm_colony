# Worm colony
### Stages:

# Release info:
## Hyperparameters, you can set in Utils.py:
* WORM_MEMORY_SIZE - Size of worm's memory storage. / Длина памяти червя.
* INITIAL_LR - Initial learning rate. / Начальный learning_rate.
* LEARN_BATCH_SIZE - Batch size for learning. / Размер батча для обучения.
* HEALTH_COEF - Coefficient for health in reward formula. / Коэффициент здоровья в формуле награды.
* SATURATION_COEF - Coefficient for saturation in reward formula. / Коэффициент насыщения в формуле награды.
* AGE_ACTIVITY - Intensivity of learning through age. / Обучаемость в большом возрасте.

* EPS - Decisioning threshold. / Порог принятия решения.
* FOOD_RESTORATION - Amount of health restored by food (when eaten). / Количество здоровья, восстанавливаемого при съедании еды.
* SPIKE_DAMAGE - Amount of health taken by hitting spike. / Количество здоровья, отнимаемого при ударе о колючку.
* WORM_DAMAGE - Amount of health taken by hitting worm (if attacks). / Количество здоровья, отнимаемого при атаке червя.
* RENDER_DELAY - Delay in ms for rendering debug picture. Works if --visual-debug-show parameter is True. / Задержка на рендеринг отладочной картинки. Используется только при включенном  --visual-debug-show.

## Reward formula:
### reward = HEALTH_COEF\*delta_health + SATURATION_COEF\*delta_saturation
## Learning rate formula:
### lr = (INITIAL_LR  - reward/float(100))\*float(AGE_ACTIVITY)/(1 + (self.time\*\*2))

## Hyperparamters, you can set from cmd:
* --worms-init-num= - Initial amount of worms (int). / Начальное количество червей.
* --food-init-num= - Initial amount of food (int). / Начальное количество еды.
* --spike-init-num= - Initial amount of spikes (int). / Начальное количество колючек.
* --worm-spawn-time= - Time for spawn new worms (int). / Время спавна новых червей.
* --food-spawn-time= - Time for spawn new food (int). /  Время спавна новой еды.
* --spike-spawn-time - Time for spawn new spikes (int). / Время спавна новых колючек.
* --worm-spawn-amount= - Amount of new worms to be spawned (int). / Количество новых спавнящихся червей.
* --food-spawn-amount= - Amount of new food to be spawned (int). /  Количество новой спавнящейся еды.
* --spike-spawn-amount= - Amount of new spikes to be spawned (int). / Количество новых спавнящихся колючек.
* --world-width= - Width of the world (int). / Ширина мира.
* --world-height= - Height of the world (int). / Высота мира.
* --learning - Whether to learn worms. / Обучать ли червей.
* --breeding - Do worms can breed. / Обучать ли червей
* --breeding-age= - Breeding age (int). / Возраст, начиная с которого черви могут размножаться.
* --world-lifespan= - Lifespan of the world (int). / Время жизни мира.
* --spike-lifespan= - Lifespan of spike (int). / Время жизни колючки.
* --food-lifespan= - Lifespan of food (int). / Время жизни еды.
* --worm-lifespan= - Lifespan of worm (int). / Время жизни червя.
* --worm-speed= - Speed of worm (int). / Скорость движения червя.
* --worm-adequacy= - Adequacy of the worm (chance to do as worm decided) (float, from 0 to 1). / Адекватность червей (шанс сделать действие, которое предпочёл червь).
* --adequacy-increase-span= - Period of worm lifespan within which the worm gets completely adequate (float, from 0 to 1). / Период жизни червя, за который он станет полностью адекватным.
* --learn-frequency= - Frequency of learning sessions (less than worm lifespan, more than LEARN_BATCH_SIZE) (int). / Время обучения червей.
* --visual-width-scale= - Scale of visual width (int). / Растяжение мира при показе по ширине.
* --visual-height-scale= - Scale of visual height (int). / Растяжение мира при показе по высоте.
* --visual-debug-show - Whether to show debug visual picture. / Показывать ли отладочную визуализацию.
* --visual-save-recap - Whether to save video recap. /  Сохранять ли видеозапись эксперимента.
* --visual-fps= - FPS rate in video recap (int). / Количество FPS в видеозаписи (больше = быстрее).

## Stats description:
* time - Time from the start of the world. / Время, прошедшее с момента старта мира.
* breedings - Amount of breedings. / Количество размножений.
* crazy_actions - Amount of crazy actions made. / Количество неадекватных действий.
* attacks - Amount of attacks made by worms to other worms. / Количество атак, произведенных червями по другим червям.
* deaths - Amount of deaths. / Количество умерших червей.
* resources_exhaustion - Amount of resources exhausted. / Количество уничтоженных ресурсов.
* population - Population of the world. If equals 0, the emulation stops. /  Общее количество червей. Если равняется 0, эмуляция прекращается.
* world_lifespan - Lifespan of the world. / Максимальное время жизни мира.
* food_eaten - Amount of hits to food. / Число съеденной еды (число укусов).
* spikes_hit - Amount of hits by spikes. / Число срабатываний колючек.
* food_spawned - Amount of food spawned. / Количество заспавненной еды.
* spiked_spawned - Amount of spikes spawned. / Количество заспавненных колючек.
