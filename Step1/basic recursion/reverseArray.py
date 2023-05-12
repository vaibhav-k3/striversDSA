def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def reverseArr(arr,i,n):
    if i <n//2:
        return
    else:
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp
        reverseArr(arr,i-1,n)



arr = inlt()
n = len(arr)
reverseArr(arr,n-1,n)
print(arr)
