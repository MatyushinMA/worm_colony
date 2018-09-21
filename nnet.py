import torch
import torch.nn as nn

class WormNET(nn.Module): # worm net class
    def __init__(self, path_to_xml): # initialize and load model
        super(WormNET, self).__init__()
        self._load_net(path_to_xml)

    def _load_net(self, path_to_xml): # loading model here
        # write parser here
        pass

    def _feed(self, x): # feed x to the net
        # write forward pass here
        return x

    def __forward__(self, x): # forward pass
        res = self._feed(x)
        return res

