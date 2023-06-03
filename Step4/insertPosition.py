def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def insertPosition(arr,k):
    insertpos=0
    low = 0
    high = len(arr)-1
    prevMid = 0
    while low < high:
        mid = (low+high)//2
        if arr[mid] == k:
            return mid
        else:
            if arr[mid] < k:
                low = mid+1
            else:
                high = mid
            
            prevMid = mid
    

    if arr[prevMid] < k :
        return prevMid + 1
    else:
        return prevMid - 1


arr = inlt()
k = inp()
print(insertPosition(arr,k))