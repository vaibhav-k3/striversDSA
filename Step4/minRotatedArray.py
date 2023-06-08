def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def minRotatedArray(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2

        if mid == len(arr) - 1:
            if arr[mid] < arr[low]:
                return arr[mid]
            else:
                return arr[low]
        if mid == 0:
            if arr[mid] < arr[high]:
                return arr[mid]
            else:
                return arr[high]
            
        if arr[mid] < arr[mid -1] and arr[mid] < arr[mid + 1]:
            return arr[mid]
        
        if arr[mid] < arr[high]:
            high = mid -1
        else:
            low = mid + 1


arr = inlt()
print(minRotatedArray(arr))