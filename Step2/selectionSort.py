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
for i in range(len(nums)):
    min = nums[i]
    min_idx = i
    for j in range(i,len(nums)):
        if nums[j]< min:
            min = nums[j]
            min_idx = j
    
    nums[i] , nums[min_idx] = nums[min_idx] , nums[i]


print(nums)