def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def makeBouquet(arr,m,k):
    if m*k > len(arr):
        return 0
    
    high = -1
    for num in arr:
        high = max(high,num)

    low = 1
    while low <= high:
        mid = (low+high)//2
        diff = 0
        cnt1 = 0
        cnt2 = 0
        total_diff = 0
        for num in arr:
            diff = num - mid
            if diff == 0:
                cnt1+=1
            else:
                cnt1=0
                total_diff+=diff

            if cnt1==k:
                cnt2+=1
                cnt1=0
        if cnt2==m:
            high = mid -1 
        else:
            low = mid + 1
    
    return low - 1



arr = inlt()
m = inp()
k = inp()
print(makeBouquet(arr,m,k))