def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def compare(nums, i , n):
    if i==n:
        return
    if nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
    compare(nums,i+1,n)


def recBubbleSort(nums , i , n):
    if i ==n:
        return
    
    compare(nums,0,n)
    recBubbleSort(nums,i+1,n)

nums = inlt()
n = len(nums)
recBubbleSort(nums, 0 , n-1)
print(nums)