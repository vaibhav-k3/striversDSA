def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def lastOccurance(arr,key):
    low = 0
    high = len(arr)-1
    res = -1
    while low < high:
        mid = (low+high)//2
        if arr[mid] == key:
            res = mid
            low = mid+1
        elif arr[mid] < key:
            low = mid+1
        else:
            high = mid
    
    return res


arr = inlt()
key = inp()
print(lastOccurance(arr,key))