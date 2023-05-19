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
sum = inp()
i = 0
j = 1
k = len(arr)-1
arr.sort()
ans = []
for i in range(len(arr)):
    j = i + 1
    k = len(arr)-1
    while j < k:
        if arr[i] + arr[j] + arr[k] == sum and i!=j and j!=k and i!=k:
            ans.append((arr[i],arr[j],arr[k]))
            j+=1
            k-=1
        elif arr[i] + arr[j] + arr[k] < sum:
            j+=1
        else:
            k-=1

print(set(ans))