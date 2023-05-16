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
ans = [0]*len(arr)
pos =[]
neg =[]

for num in arr:
    if num < 0:
        pos.append(num)
    else:
        neg.append(num)

i = 0
j = 0
arr_idx = 0
while i < len(pos) and j<len(neg):
    if arr_idx%2==0:
        ans[arr_idx] = pos[i]
        i+=1
    else:
        ans[arr_idx] = neg[j]
        j+=1
    arr_idx+=1

while i < len(pos):
    ans[arr_idx] = pos[i]
    arr_idx+=1
    pos+=1

while j < len(neg):
    ans[arr_idx] = neg[i]
    arr_idx+=1
    j+=1

print(ans)





