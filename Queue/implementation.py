from collections import deque

queue = deque(maxlen=5)

def enqueue(val):
    if len(queue) == queue.maxlen:
        print("Overflow")
        return
    queue.append(val)
    print(f"Enqueued {val}")

def dequeue():
    if len(queue) == 0:
        print("Underflow")
        return
    return queue.popleft()
    
    
# Driver
enqueue(5)
enqueue(10)
enqueue(15)
enqueue(20)
enqueue(25)
enqueue(30)

print("Deleted:", dequeue())
print(list(queue))