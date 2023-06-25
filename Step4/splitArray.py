def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def subArrayExists(arr,mid,k):
    for i in range(0,len(arr)):
        j = i
        cnt = 0
        sum=0
        while j < len(arr) and cnt < k:
            sum+=arr[j]
            j+=1
            cnt+=1
        
        max_sum = sum
        if cnt < k-1:
            return False

        while j < len(arr):
            if sum >=mid:
                return True
            sum+=arr[j]
            j+=1
        
    return False
        
    
            
            




def subArrayWithLargestSum(arr,k):
    low = min(arr)
    high = 99999999
    ans = -1
    while low <= high:
        # 
        mid = (low+high)//2
        
        if subArrayExists(arr,mid,k):
            ans = mid
            low = mid + 1
        else:
            # ans = mid
            # print(low,high,mid)
            high = mid -1
        ans = mid
    return ans

arr = inlt()
k = inp()

print(subArrayWithLargestSum(arr, k))
