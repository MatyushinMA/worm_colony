import torch
import torch.nn as nn
from collections import OrderedDict

class WormNET(nn.Module):
    def __init__(self):
        super(WormNET, self).__init__()

        # in - (batch_size, 3 - depth, 11 - width, 12 - height)
        self.features = nn.Sequential(OrderedDict([
        ('conv1', nn.Conv2d(3, 16, 3)),
        ('elu1', nn.ELU()),
        ('conv2', nn.Conv2d(16, 32, 3)),
        ('elu2', nn.ELU()),
        ('conv3', nn.Conv2d(32, 64, 3)),
        ('elu3', nn.ELU()),
        ('conv4', nn.Conv2d(64, 128, 3)),
        ('elu4', nn.ELU()),
        ('conv5', nn.Conv2d(128, 160, 3)),
        ('elu5', nn.ELU())]))
        # out - (batch_size, 160, 1, 2)
        # in - (batch_size, 2, 1, 160)
        self.turn = nn.Sequential(OrderedDict([
        ('lin1', nn.Linear(160, 80)),
        ('prelu1', nn.PReLU(2)),
        ('lin2', nn.Linear(80, 40)),
        ('prelu2', nn.PReLU(2)),
        ('lin3', nn.Linear(40, 1)),
        ('softmax', nn.Softmax(dim=1))]))
        # out - (batch_size, 2, 1, 1)
        # in - (batch_size, 2, 1, 160)
        self.move = nn.Sequential(OrderedDict([
        ('lin1', nn.Linear(160, 80)),
        ('prelu1', nn.PReLU(2)),
        ('lin2', nn.Linear(80, 40)),
        ('prelu2', nn.PReLU(2)),
        ('lin3', nn.Linear(40, 1)),
        ('softmax', nn.Softmax(dim=1))]))
        # out - (batch_size, 2, 1, 1)
        # in - (batch_size, 2, 1, 160)
        self.attack = nn.Sequential(OrderedDict([
        ('lin1', nn.Linear(160, 80)),
        ('prelu1', nn.PReLU(2)),
        ('lin2', nn.Linear(80, 40)),
        ('prelu2', nn.PReLU(2)),
        ('lin3', nn.Linear(40, 1)),
        ('softmax', nn.Softmax(dim=1))]))
        # out - (batch_size, 2, 1, 1)

    def forward(self, x):
        features = self.features(x).permute(0, 3, 2, 1)
        turn = self.turn(features)
        move = self.move(features)
        attack = self.attack(features)

        ezturn = turn[:, 0, :, :] - turn[:, 1, :, :]
        ezmove = move[:, 0, :, :] - move[:, 1, :, :]
        ezattack = attack[:, 0, :, :] - attack[:, 1, :, :]

        return [turn, move, attack], [ezturn, ezmove, ezattack]
