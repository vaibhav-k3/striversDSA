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
# Approach 1: 
# res = ['_'] * len(nums)
# cnt = 0
# for i in range(len(nums)-1):
#     if nums[i] < nums[i+1]:
#         res[cnt] = nums[i]
#         cnt+=1
# print(res)

# Approach 2

i = 0
for j in range(1,len(nums)):
    if nums[j] != nums[i]:
        i+=1
        nums[i] = nums[j]

print(nums[:i+1])