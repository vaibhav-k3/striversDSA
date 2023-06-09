def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def findKrotations(arr):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:

        mid = (low+high)//2
        if mid==0 and arr[mid] < arr[high]:
            return mid
        
        if mid == len(arr) -1 and arr[low] > arr[mid]:
            
            return mid

        if arr[mid-1] > arr[mid] and arr[mid] < arr[mid+1]:
            return mid
        
        
        if arr[mid] < arr[high]:
            high = mid - 1
        else:
            low = mid + 1

    return -1




arr = inlt()
print(findKrotations(arr))