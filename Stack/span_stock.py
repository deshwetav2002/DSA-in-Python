from collections import deque

def stock_span(arr):
    stack = deque()
    stack.append(0)
    print(1, end=" ")

    for i in range(1, len(arr)):
        while(len(stack) != 0 and arr[stack[-1]]<=arr[i]):
            stack.pop()
        
        if len(stack) == 0:
            print(i+1, end=" ")
        else:
            print(i-stack[-1], end=" ")

        stack.append(i)

size = int(input("Enter the size: "))
arr=[]
for i in range(size):
    x = int(input(f"arr{[i]} = ")) 
    arr.append(x)

stock_span(arr)