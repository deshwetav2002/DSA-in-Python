def Selectionsort(arr):
    size = len(arr)

    for i in range(0, size):
        min_index = i
        for j in range(i+1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
    return arr

arr = [1, 5, 3, 7, 9, 11]
print(Selectionsort(arr))