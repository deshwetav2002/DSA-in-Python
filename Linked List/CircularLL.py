class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertfirst(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while True:
            print (temp.data, end = " ") 
            temp = temp.next 
            if temp== self.head:
                break 


ll = LinkedList()
ll.insertfirst(10)
ll.insertfirst(20)
ll.insertfirst(30)
ll.insertfirst(40)
print(ll.head.next.data)

ll.display()
