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

def sqaureRoot(key):

    low = 1
    high = key // 2
    mid = -1
    while high - low >0:
        
        mid = (low+high)/2
        if mid*mid == key:
            return math.floor(mid)
        
        if key%(mid*mid) >= key:
            high = mid
        else:
            
            low = mid
    
    return mid




key = inp()

print(sqaureRoot(key))