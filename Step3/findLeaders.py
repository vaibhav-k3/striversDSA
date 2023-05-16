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
leaders = []
j = len(arr)-2
i = len(arr) - 1
leaders.append(arr[i])
while j >=0:
    if arr[j] > arr[i]:
        i = j
        leaders.append(arr[j])

    j-=1
print(leaders)




