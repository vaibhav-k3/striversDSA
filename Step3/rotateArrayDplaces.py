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
D = inp()
#LOL
# start_idx = len(nums)%D
# for i in range(D, D+len(nums)):
#     print(nums[i%len(nums)],end=' ',)

# Approach 1
#COPY elements
# temp_arr = []
# for i in range(0,D):
#     temp_arr.append(nums[i])


# for i in range(D,len(nums)):
#     nums[i-D] = nums[i]

# n = len(nums)
# temp_idx = 0
# for i in range(0,len(temp_arr)):
#     nums[n-D+i] = temp_arr[i]
#     temp_idx+=1

# print(nums)

# Approach 2: Reversal Algorithm
def reverse(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-1-i] = arr[n-1-i],arr[i]
    return arr

nums[0:D] = reverse(nums[0:D])
# print(nums)
nums[D:]=reverse(nums[D:])
nums = reverse(nums)

print(nums)