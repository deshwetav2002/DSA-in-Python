def prevgreater(arr, size):
    for i in range(size):
        flag = False
        
        for j in range(i-1, -1, -1):
            if arr[j] > arr[i]:
                print(arr[j], end = " ")
                flag = True
                break
        if not flag:
            print("-", end=" ")

arr = [12, 10, 20, 22, 15, 14, 18, 32]
size = len(arr)
prevgreater(arr, size)
