def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

import sys
arr = inlt()
sum = 0
max_sum = -sys.maxsize
for num in arr:
    sum+=num
    if sum < 0:
        sum=0
    max_sum = max(max_sum,sum)

print(max_sum)