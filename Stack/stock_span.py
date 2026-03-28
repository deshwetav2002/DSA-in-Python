def stock_span(arr):
    for i in range(len(arr)):
        curr_span=1
        j=i-1
        while j>=0 and arr[j]<=arr[i]:
            curr_span+=1
            j-=1
        print(curr_span, end = " ")

arr=[]
n = int(input("Enter the size: "))
for i in range(n):
    x = int(input("Enter number: "))
    arr.append(x)
    
stock_span(arr)