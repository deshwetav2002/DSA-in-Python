class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertFirst(self, data):
        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node           #changing the head to freshly entered node

    def insertLast(self, data):
        new_node = Node(data)
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next 



ll = LinkedList()

ll.insertFirst(10)
ll.insertFirst(12)
ll.insertLast(15)
ll.display()