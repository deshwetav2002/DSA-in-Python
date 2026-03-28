class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def InsertFirst(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def InsertLast(self, data):
        new_node = Node(data)
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insertatposition(self, pos, data):
        size = self.calcsize()
        if pos == 1:
            self.InsertFirst(data)
            return
        if pos<1 and size<pos:
            print("You given wrong position...")
            return
        else:
            temp = self.head
            new_node = Node(data)

            for i in range(1, pos-1):
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

    def calcsize(self):
        size = 0
        node = self.head
        while node is not None:
            node = node.next
            size+=1
        return size

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


ll = LinkedList()
ll.InsertFirst(9)
ll.InsertFirst(10)
ll.InsertFirst(11)

ll.InsertLast(5)
ll.InsertLast(6)
ll.InsertLast(7)

ll.insertatposition(1, 20)
ll.display()

        