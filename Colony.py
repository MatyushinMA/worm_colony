from Worm import Worm
from Utils import ORIENTATIONS, WORM_LENGTH

class Colony:
    def __init__(self, max_time, max_power=100):
        self._iter = 0
        self.act_id = 0
        self.act_worms = 0
        self.worms = []
        self.max_power = max_power
        self.max_time = max_time
    
    def __iter__(self):
        self._iter = 0
        return self
    
    def __next__(self):
        if self._iter >= self.act_worms:
            raise StopIteration
        w = self.worms[self._iter]
        self._iter += 1
        return w
    
    def _kill_worm_by_id(self, id):
        for i, w in self.worms:
            if w.get_id() == id:
                w.set_health(0)
                self.worms.pop(i)
                self.act_worms -= 1
                return True
        return False
    
    def get_worm_by_position(self, x, y):
        # TODO: Get worm by tail too
        for w in self.worms:
            worm_position = w.get_position()
            if worm_position[0] == x and worm_position[1] == y:
                return w
        return None
    
    def interception(self, x, y):
        inter_res = 0.
        for w in self.worms:
            worm_position = w.get_position()
            if worm_position[0] == x:
                if worm_position[1] == y:
                    inter_res += float(w.get_health())
                multiplier = 0
                if worm_position[2] == ORIENTATIONS['top']:
                    multiplier = 1
                elif worm_position[2] == ORIENTATIONS['bottom']:
                    multiplier = -1
                if not multiplier == 0:
                    for l in range(1, WORM_LENGTH):
                        if worm_position[1] == y + multiplier*l:
                            inter_res += w.get_health()/float(WORM_LENGTH)
            elif worm_position[1] == y:
                multiplier = 0
                if worm_position[2] == ORIENTATIONS['left']:
                    multiplier = 1
                elif worm_position[2] == ORIENTATIONS['right']:
                    multiplier = -1
                if not multiplier == 0:
                    for l in range(1, WORM_LENGTH):
                        if worm_position[0] == x + multiplier*l:
                            inter_res += w.get_health()/float(WORM_LENGTH)
        
        return inter_res
    
    def tick(self):
        for w in self.worms:
            w.tick()
    
    def clean_up(self):
        count = 0 
        ex_ids = []
        for w in self.worms:
            if w.get_time() > self.max_time or w.get_saturation() <= 0 or w.get_health() <= 0:
                ex_ids.append(w.get_id())
        self.kill_worm_by_id(ex_ids)
        return len(ex_ids)
    
    def emplace_worm(self, x, y, orient=0):
        self.worms.append(Worm(self.act_id, x, y, orient))
        self.act_id += 1
        self.act_worms += 1
        return True
    
    def add_worm(self, new_w):
        max_id = new_w.get_id()
        for w in self.worms:
            tmp_id = w.get_id()
            if new_w.get_id() == tmp_id:
                # id conflict
                return False
            if tmp_id > max_id:
                max_id = tmp_id
        self.worms.append(new_w)
        self.act_worms += 1
        self.act_id = max_id + 1
        return True

    def get_count_of_worms(self): 
        return self.act_worms
    
    def get_worm_by_id(self, id):
        for w in self.worms:
            if w.get_id() == id:
                return w
        return None
    
    def kill_worm_by_id(self, id):
        if isinstance(id, list):
            res = True
            for i in id:
                res = res and self._kill_worm_by_id(self, i)
            return res
        elif isinstance(id, int):
            return self._kill_worm_by_id(self, id)

