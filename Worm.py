from Nnet import WormNET
from Memory import Storage
from Utils import WORM_MEMORY_SIZE, INITIAL_LR, LEARN_BATCH_SIZE, HEALTH_COEF, SATURATION_COEF, EPS, AGE_ACTIVITY
from math import fabs

import torch
import torch.nn as nn
import numpy.random as npr

class Worm:
    def __init__(self, id, x, y, orientation=0):
        self.id = id
        self.health = 100
        self.time = 0
        self.power = 1
        self.saturation = 100
        self.orient = orientation

        self.net = WormNET()
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
        self._state['health'] = self.health - self._state['health']
        self._state['saturation'] = self.saturation - self._state['saturation']
        self.storage.push_memo(self._view, self._act, self._state)

    def learn(self):
        self.net.train()
        lbs = npr.randint(1, LEARN_BATCH_SIZE)
        learn_batch = self.storage.batch(lbs)
        for view, act, state in learn_batch:
            reward = HEALTH_COEF*state['health'] + SATURATION_COEF*state['saturation']
            if reward <= 0:
                target = [torch.zeros([1, 1, 1], dtype=torch.long), torch.zeros([1, 1, 1], dtype=torch.long), torch.zeros([1, 1, 1], dtype=torch.long)]
                for act_id in range(3):
                    if act[act_id] > EPS:
                        target[act_id][0] = 1
                    elif act[act_id] >= -EPS: # Stagnation penalty
                        target[act_id][0] = npr.randint(0, 2)
                lr = (INITIAL_LR  - reward/float(100))*float(AGE_ACTIVITY)/(1 + (self.time**2))
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
                lr = max(INITIAL_LR  - reward/float(100), 0.)*float(AGE_ACTIVITY)/(1 + (self.time**2))
                for param_group in self.optimizer.param_groups:
                    param_group['lr'] = lr

                prob, _ = self.net(view)
                loss = torch.zeros(1, requires_grad=True)
                if target[0].item() >= 0:
                    loss += self.loss_fn(prob[0], target[0])
                if target[1].item() >= 0:
                    loss += self.loss_fn(prob[1], target[1])
                if target[2].item() >= 0:
                    loss += self.loss_fn(prob[2], target[2])

                self.optimizer.zero_grad()
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

    def get_saturation(self):
        return self.saturation

    def set_saturation(self, s):
        self.saturation = s

    def get_time(self):
        return self.time

    def tick(self):
        self.time += 1

    def get_position(self):
        return (self.x, self.y, self.orient)

    def set_position(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orient = orientation
