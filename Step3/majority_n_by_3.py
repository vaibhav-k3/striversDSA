def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

from collections import defaultdict
arr = inlt()
# hash = defaultdict(int)
# ans = set()
# for num in arr:
#     hash[num]+=1
#     if hash[num] > len(arr)//3:
#         ans.add(num)

# print(ans)
arr.sort()
ans =[]
i = 0
while i < len(arr)-1:
    cnt = 1
    while i < len(arr)-1 and arr[i] == arr[i+1]:
        i+=1
        cnt+=1
    print(cnt)
    if cnt > len(arr)//3:
        ans.append(arr[i])
    i+=1

print(ans)