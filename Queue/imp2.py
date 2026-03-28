MAX = 5
queue = [None] * MAX

front = -1
rear = -1


def enqueue(x):
    global front, rear

    if rear == MAX - 1:
        print("Queue Overflow")
        return

    if front == -1:   # first insertion
        front = 0

    rear += 1
    queue[rear] = x
    print(x, "inserted")


def dequeue():
    global front, rear

    if front == -1 or front > rear:
        print("Queue Underflow")
        return

    x = queue[front]
    front += 1
    return x


def display():
    if front == -1 or front > rear:
        print("Queue Empty")
        return

    for i in range(front, rear + 1):
        print(queue[i], end=" ")
    print()

# Driver
enqueue(5)
enqueue(10)
enqueue(15)
enqueue(20)
enqueue(25)
enqueue(30)

print("Deleted:", dequeue())
display()