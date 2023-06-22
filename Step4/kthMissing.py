def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def kthmissing(arr,k):
    i = 0
    cnt = 0
    ans = - 1
    while i < len(arr) - 1:
        if arr[i+1] - arr[i] > 1:
            cnt+=1
        
            if cnt==k:
                ans = arr[i] + 1
        i+=1
    
    return ans


arr = inlt()
k = inp()
print(kthmissing(arr,k))