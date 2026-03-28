class Dictionary:
    def __init__(self, size):
        self.size = size
        self.slots= [None]*self.size
        self.data=[None]*self.size
    
    def hash_func(self, key):
        return abs(hash(key))%self.size
    
    def rehash(self, old_hash):
        return (old_hash+1) % self.size
    
    def put(self, key, value):
        hash_value = self.hash_func(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:

            if self.slots[hash_value] == key:
               self.data[hash_value] = value
            else:
                new_hash = self.rehash(hash_value)
                while self.slots[new_hash] != None and self.slots[new_hash] != key:
                    new_hash = self.rehash(new_hash)
                
                if self.slots[new_hash] == None:
                    self.slots[new_hash] = key
                    self.data[new_hash] = value
                else:
                    self.data[new_hash] = value
        
    def get(self, key):
        start_pos = self.hash_func(key)
        cur_pos = start_pos

        while self.slots[cur_pos] != None:
            if self.slots[cur_pos] == key:
                return self.data[cur_pos]
            cur_pos = self.rehash(cur_pos)

            if cur_pos == start_pos:
                return "Not found"
        return "None Not Found"
    
    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i], ":", self.data[i], end=" ")
        return " "
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, value):
        self.put(key, value)

D=Dictionary(3)

D['python'] = 1000
D['Java'] = 200
D["c"] = 500
print(D["Java"])
print(D.slots)
print(D.data)


