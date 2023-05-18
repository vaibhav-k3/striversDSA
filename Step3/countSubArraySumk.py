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
k = inp()
hash = {}
sum = 0
cnt = 0
i =0
for num in arr:
    sum+=num
    if sum == k:
        cnt+=1
    
    hash[sum]=i
    diff = sum - k
    if diff in hash.keys():
        cnt+=1

print(cnt)

