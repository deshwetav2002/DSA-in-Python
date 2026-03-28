def bs(arr, key):
    size = len(arr)
    l = 0
    r = size-1

    while l<=r:
        mid = (l+r)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            r = mid-1
        elif arr[mid] < key:
            l = mid+1
    return -1

arr = [1, 3, 5, 7, 9, 11, 15]
key = int(input("Enter the number to searched: "))
result = bs(arr, key)
print(f"The number {key} is present in {result} index")