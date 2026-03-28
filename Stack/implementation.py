from sys import maxsize  #used to return -infinite when stack is empty 

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0      #Boolean condition(return True or False)

def push(stack, item):          #Just append items
    stack.append(item)
    print(f"{item} is pushed")

def pop(stack):         #Returns last item or element of the list
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack.pop()

def peek(stack):            #Returns the top element
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack[len(stack)-1]

stack = createStack()
push(stack, 5)  #we can use str(5), if we apply concatenation(+)
push(stack, 10)
push(stack, 15)
push(stack, 20)
push(stack, 25)
push(stack, 30)
print(stack)
print(f"Peek item is: {peek(stack)}")
print(f"{pop(stack)} is popped, new stack is-")
print(stack)
print(f"Peek item is: {peek(stack)}")