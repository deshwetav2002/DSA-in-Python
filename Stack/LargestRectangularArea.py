def maxArea(arr, size):
    res = 0

    for i in range(size):
        count = 1
        for j in range(i-1, -1, -1):
            if arr[j] >= arr[i]:
                count +=1
            else:
                break

        for j in range(i+1,size):
            if arr[j] >= arr[i]:
                count +=1
            else :
                break

        temp = count * arr[i]
        res = max(res, temp)

    return res


# Driver code
arr = [12, 3, 4, 4, 1, 5, 7]
print("Max Area: ", maxArea(arr, len(arr)))