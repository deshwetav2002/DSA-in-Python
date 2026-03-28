def rev(arr, size, i):
    if i==size:
        return 
    else:
        rev(arr, size, i+1)
        print(f"{arr[i]}")

arr = [1,2,3,4,5]
size = len(arr)
print(rev(arr, size, 0))