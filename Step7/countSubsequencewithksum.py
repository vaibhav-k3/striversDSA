def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))



def countSubsequnece(arr,k,i):
    if i <0:
        if k == 0:
            return 1
        else:
            return 0
    left_sum = 0
    if k>0:
        left_sum = countSubsequnece(arr,k-arr[i],i-1)
    right_sum = countSubsequnece(arr,k,i-1)
    return left_sum + right_sum

arr = inlt()
k = inp()
print(countSubsequnece(arr,k,len(arr)-1))