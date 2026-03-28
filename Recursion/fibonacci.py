def fibonacci(n):
    if n>1:
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        if n==0:
            return 0
        else:
            return 1
        
n = 6
a = fibonacci(n)
print(f"{n}th fibonacci number is {a}")