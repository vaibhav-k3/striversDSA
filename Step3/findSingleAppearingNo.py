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
res = arr1[0]
for num in arr1[1:]:
    res = res^num
print(res)