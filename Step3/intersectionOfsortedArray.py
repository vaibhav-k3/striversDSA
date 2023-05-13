def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


arr1 = inlt()
arr2 = inlt()

result =[]
i = 0
j = 0

n = len(arr1)
m = len(arr2)
last_add = None

while i < n and j < m:
    if arr1[i] == arr2[j]:
        result.append(arr1[i])
        last_add = arr1[i]
        i+=1
        j+=1

    elif arr1[i] < arr2[j]:
        i+=1
    else:
        j+=1

print(result)

