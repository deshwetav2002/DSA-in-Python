def linear_search(arr, length, item):
    for i in range(0, length):
        if arr[i] == item:
            return i
    else:
        return -1

arr = [1, 4, 6, 78, 45, 65, 3]
item=int(input("Enter the number: "))
length = len(arr)
result = linear_search(arr, length, item)

if result == -1:
    print(f"The number {item} is not found")
else:
    print(f"The number {item} is present in {result} idex")
