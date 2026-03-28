def findvalue(arr, i, val):
    if i == -1:
        return -1
    if arr[i] == val:
        return i
    return findvalue(arr, i-1, val)

arr = [2, 5, 3, 6, 4, 5]
size = len(arr)
val = int(input("Enter the number: "))

index = findvalue(arr, size-1, val)
if index != -1:
    print(f"The value {val} is found at index {index}.")
else:
	print(f"The value {val} is not in the array.")

