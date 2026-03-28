class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_ll:
    def __init__(self):
        self.head = None
    
    def insertstart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        temp = self.head

        if self.head != None:
            temp.prev = new_node
        
        self.head = new_node
    
    def insertlast(self, data):
        new_node = Node(data)
        new_node.next = None
        new_node.prev = None

        #if no node is present
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display (self):
        temp = self.head 
        end = None 
        print ("Linked List in Forward Direction") 
        while temp:
            print (temp.data, end = " ") 
            end = temp 
            temp = temp.next 
        print ("") 
	  
        print ("Linked List in backward direction") 
        while end:
            print (end.data, end = " ") 
            end = end.prev 
        print ("") 
    
ll = Doubly_ll()
ll.insertstart(10)
ll.insertstart(20)
ll.insertstart(30)

ll.insertlast(50)

ll.display()