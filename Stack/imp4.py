from collections import deque

stack = deque()

stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)

print(stack)

top = stack[-1]
print(top)

print(f"{stack.pop()} is popped")
print(stack)
print(f"The top element is: {stack[-1]}")