def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


# Do without sorting
import sys
nums = inlt()
second_largest = -sys.maxsize
largest = -sys.maxsize

smallest = sys.maxsize
second_smallest = sys.maxsize

for i in range(len(nums)):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif second_largest < nums[i] and nums[i]!=largest:
        second_largest = nums[i]

    if nums[i] < smallest:
        second_smallest = smallest
        smallest = nums[i]
    elif second_smallest > nums[i] and nums[i]!=smallest:
        second_smallest = nums[i]

if len(nums) != 0:
    print(second_smallest, second_largest)
