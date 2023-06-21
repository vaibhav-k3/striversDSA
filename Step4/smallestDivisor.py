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

def smallestDivisor(arr,k):
    low = 1
    high = 99999
    while low <= high:
        mid = (low+high)//2
        sum = 0
        for num in arr:
            sum += math.ceil(num/mid)
        
        if sum < k:
            high = mid - 1
        
        else:
            low = mid + 1
    
    return low




arr = inlt()
k = inp()
print(smallestDivisor(arr,k))