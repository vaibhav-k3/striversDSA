def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

import copy
def combinationSum1(arr,target,ans,i,ds):
    if i >= len(arr):
        if target == 0 :
            ans.append(copy.deepcopy(ds))
        return
    
    if arr[i] <= target:
        ds.append(arr[i])
        combinationSum1(arr,target-arr[i],ans,i,ds)
        ds.pop()

    combinationSum1(arr,target,ans,i+1,ds)
    

arr = inlt()
target = inp()
ans = []
ds = []
combinationSum1(arr, target, ans, 0,ds)
print(ans)