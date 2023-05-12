def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def recursiveInsertion(nums, i , n):
    if i == n+1:
        return
    temp = nums[i]
    j = i
    while j>0 and temp < nums[j-1]:
        nums[j] = nums[j-1]
        j-=1
    nums[j] = temp
    recursiveInsertion(nums,i+1,n)


nums = inlt()
recursiveInsertion(nums, 1, len(nums)-1)
print(nums)