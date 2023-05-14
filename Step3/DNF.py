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
i = 0
j = 0
while j < len(arr):
    if arr[j] == 0:
        arr[i],arr[j] = arr[j], arr[i]
        i+=1
    j+=1

j = i
while j < len(arr):
    if arr[j]==1:
        arr[i],arr[j] = arr[j], arr[i]
        i+=1
    j+=1

print(arr)

