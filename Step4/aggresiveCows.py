def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def canPlaceCows(stalls,k,mid):
    lastPos = stalls[0]
    cowsCount = 1
    i = 0
    for pos in stalls[1:]:
        if pos - lastPos >= mid:
            lastPos = pos
            cowsCount+=1


    if cowsCount == k:
        return True
    else:
        return False

def minimumDistance(stalls,k):
    stalls.sort()
    low = 1
    high = max(stalls)
    ans = -1
    while low <=high:
        mid = (low+high)//2
        if canPlaceCows(stalls,k,mid):
            low = mid + 1
            ans = mid
        else:
            high = mid - 1

    return ans

stalls = inlt()
k = inp()
print(minimumDistance(stalls,k))