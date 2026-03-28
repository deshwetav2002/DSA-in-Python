class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            return
        
        new_node.next = self.head.next
        self.head.next = new_node

        temp = self.head.data
        self.head.data = new_node.data
        new_node.data = temp
    
    def insertatEnd(self, data):
        # Naive approach
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = new_node
        new_node.next = self.head

    def endinsert(self, data):
        #Optimized approach
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            return
        
        new_node.next = self.head.next
        self.head.next = new_node

        new_node.data, self.head.data = self.head.data, new_node.data
        self.head = new_node

    def headDeletion(self):
        # Naive approach
        if self.head == None:
            print("List is empty")
            return
        
        if self.head.next == self.head:
            deleted_value = self.head.data
            self.head = None
            print(f"Deleted value: {deleted_value}")
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        deleted_value = self.head.data
        temp.next = self.head.next
        self.head = temp.next
        print(f"Deleted value: {deleted_value}")

    def delend(self):
        #optimized approach
        if self.head == None:
            return

        if self.head.next == self.head:
            deleted_val = self.head.data
            self.head = None
            print(f"Deleted value: {deleted_val}")
            return
        deleted_val = self.head.data
        self.head.data = self.head.next.data  #exchange of datas between head and head.next node is done
        self.head.next = self.head.next.next
        print(f"Deleted value: {deleted_val}")

    def deleteNode(self, pos):
        size = self.calcsize()
        if self.head == None:
            print("Empty List")
            return
        
        #if head node needs to delete
        if pos == 1:
            self.headDeletion()
            return
        
        if pos<1 or pos>size:
            print("Wrong input")
            return
        
        temp = self.head
        for i in range(pos-2):
            temp = temp.next
        deleted_value = temp.next.data
        temp.next = temp.next.next
        print(f"Deleted value: {deleted_value}")

    def calcsize(self):
        size = 0
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            size+=1
        return size


    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while True:
            print (temp.data, end = " ") 
            temp = temp.next 
            if temp== self.head:   #only for circular LL
                break 


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
# print(ll.head.next.data)
ll.insertatEnd(50)
ll.endinsert(60)
# ll.headDeletion()
# ll.delend()
ll.deleteNode(2)

ll.display()
