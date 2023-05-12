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

for i in range(1,n):
    j = i
    temp = nums[j]
    while j > 0 and temp <  nums[j-1] :
        nums[j] = nums[j-1]
        j-=1
    
    # j+=1
    nums[j] = temp

print(nums)
