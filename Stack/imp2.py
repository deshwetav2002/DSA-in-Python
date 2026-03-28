from sys import maxsize

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        print(f"{item} is pushed into stack")

    def pop(self):
        if self.isEmpty():
            return str(-maxsize-1)
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return -maxsize-1
        return self.stack[len(self.stack)-1]

    def display(self):
        print(", ".join(self.stack[i] for i in range(len(self.stack)-1, -1, -1)))
    

s = Stack()
s.push(str(5))  #we can use str(5), if we apply concatenation(+)
s.push(str(10))
s.push(str(15))
s.push(str(20))
s.push(str(25))
s.push(str(30))
s.display()
print(f"Peek item is: {s.peek()}")
print(f"{s.pop()} is popped, new stack is-")
s.display()
print(f"Peek item is: {s.peek()}")