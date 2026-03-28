MAX = 5

queue = [None]*MAX

front, rear = -1, -1

def enqueue(val):
    global front, rear

    if (rear+1) % MAX == front:
        print("Queue Overflow")
        return
    
    #first element insertion
    if front == -1:
        front = rear = 0
    else:
        rear = (rear+1) % MAX
    
    queue[rear] = val
    print(f"{val} inserted in queue")

def dequeue():
    global front, rear

    if front==-1:
        print("Stack underflow")
        return
    
    x = queue[front]

    # If only one element
    if front == rear:
        front = rear = -1
    else:
        front = (front+1) % MAX
    
    return x

def display():
    if front == -1:
        print("Empty queue")
        return
    i = front 
    while True:
        print(queue[i], end=" ")

        if i == rear:
            break
        i = (i+1) % MAX

    print()

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
enqueue(50)

display()

print("Deleted:", dequeue())
print("Deleted:", dequeue())

enqueue(60)
enqueue(70)

display()
