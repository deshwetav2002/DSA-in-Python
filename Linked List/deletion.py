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

    def deltionVal(self, delval):
        temp = self.head
        # prev = None

        #case 1: only one node
        if temp.next is None:
            self.head = None
            print(f"deleted vaue is {delval}")
            return
        
        #case 2: Multiple Node but head node needs to delete
        if temp != None and temp.data == delval:
            self.head = temp.next
            print(f"deleted vaue is {delval}")
            return
        
        #case 3: Multiple Node, Node is in middle
        while temp!=None and temp.data !=delval:
            prev = temp
            temp = temp.next
        
        if temp == None:
            print("Value not found")
            return
        
        prev.next = temp.next
        return 
    
    def deletepos(self, pos):
        temp = self.head
        prev = None
        size = self.calcsize()
        #case 1: if head node needs to be deleted
        if pos == 1:
            self.head = temp.next
            print(f"Deleted value is {temp.data}")
            return
        
        if pos < 1 or size < pos:
            print("Wrong input")
            return
        
        else:
            for i in range(1, pos-1):
                temp = temp.next
            deleted_node = temp.next
            temp.next = temp.next.next
            print(f"Deleted value is {deleted_node.data}")
            return
        


    def calcsize(self):
        size = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            size+=1
        return size        

    def display(self):
        temp = self.head
        if temp is None:
            print("Value is not present")
            return
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

ll = LinkedList()
ll.InsertFirst(5)
ll.InsertFirst(15)
ll.InsertFirst(25)
ll.InsertFirst(35)
# ll.deltionVal(35)
ll.deletepos(2)
print("\n")
ll.display()