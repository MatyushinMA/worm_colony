from Spike import Spike
from Food import Food

class Thread:
    def __init__(self, max_times):
        self.ids = {'spike' : 0, 'food' : 0}
        self.counts = {'spike' : 0, 'food' : 0}
        self.lists = {'spike' : [], 'food' : []}
        self.max_times = max_times
    
    def _add_cust(self, new_element, ident):
        max_id = new_element.get_id()
        for element in self.lists[ident]:
            tmp_id = element.get_id()
            if new_element.get_id() == tmp_id:
                # id conflict
                return False
            if tmp_id > max_id
                max_id = tmp_id
        self.lists[ident].append(new_element)
        self.ids[ident] = max_id + 1
        self.counts[ident] += 1
        return True
    
    def _emplace_cust(self, x, y, ident):
        new_element = None
        if ident == 'spike':
            new_element = Spike(self.ids[ident], x, y)
        elif ident == 'food':
            new_element = Food(self.ids[ident], x, y)
        if not new_element:
            return False
        self.lists[ident].append(new_element)
        self.ids[ident] += 1
        self.counts[ident] += 1
        return True
    
    def _delete_cust_by_id(self, id, ident):
        for i, element in enumerate(self.lists[ident]):
            if element.get_id() == id:
                self.lists[ident].pop(i)
                return True
        return False
    
    def _get_cust_by_id(self, id, ident):
        for element in self.lists[ident]:
            if element.get_id() == id:
                return element
        return None
    
    def tick(self):
        for sp in self.lists['spike']:
            sp.tick()
        for f in self.lists['food']:
            f.tick()
    
    def clean_up(self):
        ex_lists = {'spike' : [], 'food' : []}
        for sp in self.lists['spike']:
            if sp.get_time() > max_times['spike']:
                ex_lists['spike'].append(sp.get_id())
        for f in self.lists['food']:
            if f.get_time() > max_times['food']:
                ex_lists['food'].append(f.get_id())
        for sp_id in ex_lists['spike']:
            self.delete_spike_by_id(sp_id)
        for f_id in ex_lists['food']:
            self.delete_food_by_id(f_id)
        return len(ex_lists['spike'] + ex_lists['food'])
    
    # adding methods
    def add_spike(self, spike):
        return _add_cust(spike, 'spike')
    
    def add_food(self, food):
        return _add_cust(food, 'food')
    
    # emplacing methods
    def emplace_spike(self, x, y):
        return _emplace_cust(x, y, 'spike')
    
    def emplace_food(self, x, y):
        return _emplace_cust(x, y, 'food')
    
    # removing methods
    def delete_food_by_id(self, id):
        return _delete_cust_by_id(id, 'food')
    
    def delete_spike_by_id(self, id):
        return _delete_cust_by_id(id, 'spike')
    
    # geting methods
    def get_food_by_id(self, id):
        return _get_cust_by_id(id, 'food')

    def get_spike_by_id(self, id):
        return _get_cust_by_id(id, 'spike')

