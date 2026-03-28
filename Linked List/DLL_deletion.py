class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
    
    def insertFirst(self, data):
        temp = self.head
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if temp is not None:
            self.head.prev = new_node

        self.head = new_node

    def delete(self, delval):
        temp = self.head
        prev = None

        if temp is None:
            return
        
        #if only one node is present
        if temp==None and temp.data==delval:
            deleted_val = temp
            self.head = None
            print(f"Deleted value is {temp.data}")
            return

        #if head needs to delete
        if temp!=None and temp.data==delval:
            deleted_val = temp
            self.head = temp.next
            self.head.prev = None
            print(f"Deleted value is {temp.data}")
            return

        #if node is in middle or last
        while temp!=None and temp.data!=delval:
            prev = temp
            temp = temp.next     

        #if node is not present 
        if temp is None:
            print("Value not found") 
            return   

        #if last node needs to delete
        if temp.next == None:
            deleted_val = temp
            temp.prev.next = None
            print(f"Deleted value is {temp.data}")
            return
        
        #if the node is in middle
        else:
            deleted_val = temp
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            print(f"Deleted value is {temp.data}")
            return
        

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

ll = DLL()
ll.insertFirst(10)
ll.insertFirst(15)
ll.insertFirst(20)
ll.insertFirst(30)
ll.insertFirst(40)
ll.insertFirst(50)
ll.delete(20)

ll.display()