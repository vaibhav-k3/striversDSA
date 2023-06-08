def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def lowerBound(arr,low, high , key):
    prev_key = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= key:
            high = mid - 1
            prev_key = mid
        else:
            low = mid+1
    return prev_key

arr = inlt()
key = inp()
print(lowerBound(arr,0,len(arr)-1,key))