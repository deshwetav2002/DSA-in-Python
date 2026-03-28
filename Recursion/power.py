def power(x, n):
    if n != 0:
        return x*power(x, n-1)
    else:
        return 1
    
a = power(2, 3)
print(a)