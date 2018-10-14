from Worm import Worm

class Colony:
    def __init__(self, max_power, max_time):
        self.act_id = 0
        self.act_worms = 0
        self.worms = []
        self.max_power = max_power
        self.max_time = max_time
    
    def _kill_worm_by_id(self, id):
        for i, w in self.worms:
            if w.get_id() == id:
                w.set_health(0)
                self.worms.pop(i)
                self.act_worms -= 1
                return True
        return False
    
    def tick(self):
        for w in worms:
            w.tick()
    
    def clean_up(self):
        count = 0 
        ex_ids = []
        for w in self.worms:
            if w.get_time() > self.max_time or w.get_saturation() <= 0:
                ex_ids.append(w.get_id())
        self.kill_worm_by_id(ex_ids)
        return len(ex_ids)
    
    def emplace_worm(self, x, y):
        self.worms.append(Worm(self.act_id, x, y))
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

