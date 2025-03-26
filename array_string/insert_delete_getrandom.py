import random 

class RandomizedSet:

    def __init__(self):
        self.elems = []
        self.pos = {}
        
    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.pos[val] = len(self.elems)
        self.elems.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        last_elem = self.elems[-1]
        deleted_elem_idx = self.pos[val]

        self.pos[last_elem] = deleted_elem_idx
        self.elems[deleted_elem_idx] = last_elem

        self.pos.pop(val)
        self.elems.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.elems) 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()