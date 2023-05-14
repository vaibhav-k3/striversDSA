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
element = None
cnt = 0
for num in arr:
    if element is None or cnt==0:
        element = num
        cnt+=1
    else:
        cnt-=1

print(element)