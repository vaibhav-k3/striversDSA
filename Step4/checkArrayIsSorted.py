def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def checkSorted(arr, low , high):
    if low > high:
        return 1
    else:
        mid = (low+high)//2
        if  arr[mid] >= arr[low] and arr[mid] <= arr[high]:
            res1 = checkSorted(arr,low,mid-1)
            res2 = checkSorted(arr,mid+1,high)
            return res1 and res2
        else:
            return 0



arr = inlt()
print(checkSorted(arr,0,len(arr)-1))