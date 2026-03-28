from collections import deque
def celebrity(L):
    s = deque()
    for i in range(len(L)):
        s.append(i)
    
    while len(s)>=2:
        i = s.pop()
        j = s.pop()

        if L[i][j] == 0:
            #j is not celebrity
            s.append(i)
        else:
            #i is not celebrity
            s.append(j)
    
    celeb = s.pop()

    for i in range(len(L)):
        if i!=celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                print("No celebrity found")
                return
    print(f"Celebrity is {celeb}")

L = [
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
]
celebrity(L)