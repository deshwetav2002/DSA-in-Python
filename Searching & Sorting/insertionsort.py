def Insertionsort(arr):
    size = len(arr)
    
    for i in range(1, size):
        j = i-1
        while j>=0:
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                break
            j=j-1
    return arr

arr = [1, 5, 3, 7, 9, 11, 2, 16]
print(Insertionsort(arr))