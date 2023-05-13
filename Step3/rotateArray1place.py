def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


nums = inlt()
n = len(nums)
if n != 1:

    temp = nums[0]
    for i in range(1,n):
        nums[i-1] = nums[i]

    nums[n-1] = temp

print(nums)
    