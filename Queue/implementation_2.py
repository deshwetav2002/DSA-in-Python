MAX = 5

queue = [None] * MAX

front, rear = -1, -1

def enqueue(val):
    global front, rear

    if rear == MAX-1:
        print("Stack overflow") 
        return
    
    if front == -1:
        front = 0
    rear+=1
    queue[rear] = val
    print(f"{val} inserted")

def dequeue():
    global front, rear

    if front==-1 or front > rear:
        print("Underflow")
        return
    x = queue[front]
    front+=1
    return x

def display():
    if front ==-1 or front > rear:
        print("Queue is empty")
        return
    print("Queue: ")
    for i in range(front, rear+1):
        print(queue[i], end = " ")
    print()


# Driver
enqueue(5)
enqueue(10)
enqueue(15)
enqueue(20)
enqueue(25)
display()
print("Deleted:", dequeue())
enqueue(30)
display()   
print("Deleted:", dequeue())
print("Deleted:", dequeue())
print("Deleted:", dequeue())
print("Deleted:", dequeue())
print("Deleted:", dequeue())
display() 