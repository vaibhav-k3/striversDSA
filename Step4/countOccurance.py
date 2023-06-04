def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def countOccurance(arr, key):
    low = 0
    high = len(arr) - 1
    index = -1
    while low < high:
        mid = (low+high)//2
        if arr[mid]==key:
            index = mid
            break
        elif arr[mid] < key :
            low = mid + 1
        else:
            high = mid - 1
    
    if index == -1:
        return index
    

    count = 0
    temp = index
    # check front
    while arr[temp] == key and temp < len(arr):
        temp+=1
        count+=1

    # check back
    temp = index
    while temp >= 0 and arr[temp] == key:
        temp-=1
        count+=1

    return count - 1



arr = inlt()
key = inp()
print(countOccurance(arr,key))