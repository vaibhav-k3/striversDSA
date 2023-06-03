def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


arr = inlt()
x = inp()

def BinarySearch(arr, low, high ,key):
    if low >high :
        return False
    else:
        mid = (low+high)//2
        if arr[mid]==key:
            return True
        elif arr[mid] < key:
            return BinarySearch(arr, mid+1,high,key)
        elif arr[mid]> key:
            return BinarySearch(arr,low,mid,key)

print(BinarySearch(arr,0,len(arr)-1,x))