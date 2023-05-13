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
k = inp()
# hash = {}
# sum = 0
# max_length = 0
# length = 0
# for i in range(len(arr)):
#     sum+=arr[i]
#     length +=1
#     if sum == k:
#         max_length = max(max_length, i+1)
    
#     hash[sum] = i
#     rem = sum - k
#     if rem in hash.keys():
#         x = i - hash[rem]
#         max_length = max(max_length,x)

# print(max_length)


# USING 2 POINTERS
i = 0
j = 0
sum = 0
length = 0
max_length = 0
while j < len(arr):
    sum+=arr[j]
    while sum > k and i <=j:
        sum-=arr[i]
        i+=1
    if sum == k:
        max_length = max(max_length,j-i)
    j+=1

print(max_length+1)
