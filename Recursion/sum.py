def add(n):
    if n != 0:
        return n+add(n-1)            # n(n=1)/2
    else:
        return 0         

a = add(10)
print(a)