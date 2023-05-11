def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


import math

n = inp()

sqrt = math.sqrt(n)

for i in range(1,int(sqrt)):
    if n%i==0:
        print(i)
        if n//i != sqrt:
            print(n//i)