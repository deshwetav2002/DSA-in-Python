def bubblesort(arr):
    size = len(arr)
    for i in range(1, size):
        for j in range(0, size-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

arr = [1, 5, 3, 7, 9, 11]
print(bubblesort(arr))