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
max_seq = 0
seq = 0
for num in arr1:
    if num==1:
        seq+=1
        max_seq = max(max_seq, seq)
    else:
        seq = 0

print(max_seq)
