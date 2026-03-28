class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class LL:
    def __init__(self):
        self.head = None
    
    def add(self, key, value):
        new_node = Node(key, value)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
    def delete_head(self):
        if self.head == None:
            return "Empty"
        else:  
            self.head = self.head.next
        
    def remove(self, key):
        if self.head.key == key:
            self.delete_head()
        else:
            temp = self.head
            while temp.next != None:
                if temp.next.key == key:
                    break
                temp = temp.next
            if temp.next == None:
                return "Empty"
            temp.next = temp.next.next
    
    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.key,"-->",temp.value," ", end=" ")
            temp = temp.next

    def size(self):
        counter = 0
        temp = self.head
        while temp != None:
            counter+=1
            temp = temp.next
        return counter
    
    def search(self, key):
        temp = self.head
        pos = 0
        while temp != None:
            if temp.key == key:
                return pos
            pos+=1
            temp = temp.next
        return -1
    
    def get_node_at_index(self, index):
        temp = self.head
        pos = 0
        while temp != None:
            if pos == index:
                return temp
            temp = temp.next
            pos+=1

class Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        #create array of LL
        self.bucket = self.make_array(capacity)

    def make_array(self, capacity):
        L = []
        for i in range(capacity):
            L.append(LL())
        return L
    
    def hash_func(self, key):
        return abs(hash(key))%self.capacity
    
    def get_node_index(self, bucket_index, key):
        node_index = self.bucket[bucket_index].search(key)
        return node_index
   
    def put(self, key, value):
        bucket_index = self.hash_func(key)
        node_index = self.get_node_index(bucket_index, key)
        
        if node_index == -1:
            #insert
            self.bucket[bucket_index].add(key, value)
            self.size += 1
        else:
            node = self.bucket[bucket_index].get_node_at_index(node_index)
            node.value = value
    
    def get(self, key):
        bucket_index = self.hash_func(key)
        res = self.bucket[bucket_index].search(key)

        if res == -1:
            return "Empty"
        else:
            node = self.bucket[bucket_index].get_node_at_index(res)
            return node.value
        
    def delete(self, key):
        bucket_index = self.hash_func(key)
        self.bucket[bucket_index].remove(key)
        self.size -= 1
    
    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        bucket_index = self.hash_func(key)
        self.bucket[bucket_index].remove(key) 

    def __len__(self):
        return self.size()       

    def __str__(self):
        for i in self.bucket:
            i.traverse()
        return " "

    
D = Dictionary(4)

D.put("c",1000)
D.put("a",200)
D.put("b",500)

print(D)
# del D["a"]
print("a =", D["a"])   # get
D.delete("a")      # delete

print(D)