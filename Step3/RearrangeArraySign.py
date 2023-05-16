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
pos_idx = 0
negative_idx = 1
ans = [0]*len(arr)
for i in range(len(arr)):
    if arr[i] > 0:
        if pos_idx < len(arr):
            ans[pos_idx]=arr[i]
            pos_idx+=2
    else:
        if negative_idx < len(arr):
            ans[negative_idx]=arr[i]
            negative_idx+=2
print(ans)