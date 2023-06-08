def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


# def rotatedSearch(arr,low,high,key):
#     if low > high:
#         return -1
#     else:
#         mid = (low+high)//2
#         if arr[mid] == key:
#             return mid
#         else:
#             leftSearch = rotatedSearch(arr,low,mid-1,key)
#             rightSearch = rotatedSearch(arr,mid+1,high,key)
            
#             result = leftSearch if leftSearch!=-1 else rightSearch
#             return result


def rotatedSearch(arr,key):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == key:
            ans = mid
            return ans
        elif arr[low] <= arr[mid]:
            if arr[low] <= key and key <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] <= arr[high]:
            if arr[mid] <=key and key <=arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return ans
            



arr = inlt()
key = inp()

# print(rotatedSearch(arr,0,len(arr)-1, key))
print(rotatedSearch(arr, key))