from collections import deque

def reverse(queue):
    stack = []

    while queue:
        stack.append(queue.popleft())
    
    while stack:
        queue.append(stack.pop())
    
queue = deque([10, 20, 30, 40, 50])
reverse(queue)
print(queue)