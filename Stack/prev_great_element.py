from collections import deque

def prev_great(arr):
    stack = deque()
    stack.append(arr[0])
    print("-", end=" ")

    for i in range(1, len(arr)):
        while( len(stack)!=0 and stack[-1]<=arr[i]):
            stack.pop()
        
        if len(stack) == 0:
            print("-", end=" ")
        else:
            print(stack[-1], end=" ")
        
        stack.append(arr[i])

arr = [12, 10, 20, 22, 15, 14, 18, 32]
prev_great(arr)