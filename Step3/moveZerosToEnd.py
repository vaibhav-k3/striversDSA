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

# Brute Approach
# n = len(nums)
# temp = [0] * n
# temp_idx = 0
# for i, num in enumerate(nums):
#     if num != 0:
#         temp[temp_idx] = num
#         temp_idx+=1

# print(temp)

zero_idx  = 0 
while nums[zero_idx] != 0:
    zero_idx+=1

j = zero_idx
while zero_idx < len(nums) and j <  len(nums):
    if nums[j] !=0:
        nums[zero_idx],nums[j] = nums[j] , nums[zero_idx]
        zero_idx+=1
    j+=1

print(nums)


