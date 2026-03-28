from collections import deque


def nextGreater(arr, size):
    stack = deque()
    list = []

    stack.append(arr[size - 1])
    list.append("-")

    for i in range(size-2, -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()

        if len(stack) == 0:
            list.append("-")
        else:
            list.append(stack[-1])

        stack.append(arr[i])

    list.reverse()
    # print(" ".join(str(x) for x in list))
    print(list)    #['-', 25, 25, '-', 50]


# Driver code
arr = [30, 50, 20, 15, 25]
nextGreater(arr, len(arr))