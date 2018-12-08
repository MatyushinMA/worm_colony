import numpy as np
import numpy.random as npr
from operator import itemgetter

class Storage:
    def __init__(self, size):
        self.size = size
        self.inputs = []
        self.outputs = []
        self.rewards = []

    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self):
        if self._iter >= len(self):
            raise StopIteration
        memo = self[self._iter]
        self._iter += 1
        return memo

    def __getitem__(self, id):
        i = self.inputs[id]
        o = self.outputs[id]
        r = self.rewards[id]
        memo = (i, o, r)
        return memo

    def __len__(self):
        return len(self.inputs)

    def batch(self, batch_size):
        indices = npr.randint(1, len(self), batch_size).tolist()
        if len(indices) == 1:
            id = indices[0]
            return [(self.inputs[id], self.outputs[id], self.rewards[id])]
        iss = (itemgetter(*indices))(self.inputs)
        oss = (itemgetter(*indices))(self.outputs)
        rss = (itemgetter(*indices))(self.rewards)
        memos = []
        for i in range(len(indices)):
            input = iss[i]
            output = oss[i]
            reward = rss[i]
            memos.append((input, output, reward))
        return memos

    def push_memo(self, inputs, outputs, rewards):
        if len(self) == self.size:
            self.poll()
        self.inputs.append(inputs)
        self.outputs.append(outputs)
        self.rewards.append(rewards)

    def poll(self):
        self.inputs = self.inputs[1:]
        self.outputs = self.outputs[1:]
        self.rewards = self.rewards[1:]

    def getitem(self, id):
        return self.__getitem__(id)

    def iter(self):
        return self.__iter__()

    def next(self):
        return self.__next__()

    def len(self):
        return self.__len__()
