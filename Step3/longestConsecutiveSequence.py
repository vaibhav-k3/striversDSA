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

hash = {}
for num in arr:
    hash[num] = True

longestSeqLength = 0
seqlength = 0
longestSeq = []

for num in arr:
    if num-1 not in hash.keys():
        seqlength = 1
        seq = [num]
        x = num
        while x+1 in hash.keys():
            seqlength+=1
            seq.append(x+1)
            x+=1
        if seqlength > longestSeqLength:
            longestSeq = seq
            longestSeqLength = seqlength

print(longestSeq)