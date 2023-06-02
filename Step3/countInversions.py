def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def merge(arr , low , mid , high):
    l1 = mid - low + 1
    l2 = high - mid
    inversions = 0
    left = [0]*l1
    right = [0]*l2

    for i in range(l1):
        left[i] = arr[low+i]

    for i in range(l2):
        right[i] = arr[mid+i+1]

    i = j = k = 0
    k = low
    while i < l1 and j < l2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            inversions = inversions + (l1 -i)
            arr[k] = right[j]
            j+=1
        k+=1
    
    while i < l1:
        arr[k] = left[i]
        k+=1
        i+=1
    
    while j < l2:
        arr[k] = right[j]
        k+=1
        j+=1

    return inversions



def countInversions(arr , low , high):
    inversions = 0
    if low < high:
        mid = (low+high)//2
        inversions = inversions + countInversions(arr, 0 , mid)
        inversions = inversions + countInversions(arr,mid+1,high)
        inversions = inversions + merge(arr,low,mid,high)
    return inversions

arr = inlt()
inversions = countInversions(arr,0,len(arr)-1)
print(arr)
print(inversions)