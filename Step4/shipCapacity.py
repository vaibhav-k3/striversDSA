def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def findCapacity(weights,d):
    low = 1
    high = 9999999
    while low <=high:
        mid = (low+high)//2
        weight_sum = 0
        days = 1
        i = 0
        for num in weights:
            weight_sum+=num
            if weight_sum > mid:
                days+=1
                weight_sum = 0
           

        
        if days <= d:
            high = mid -1
        # elif days == d:
        #     return mid
        else:
            low = mid + 1

    
    return low
            


weights = inlt()
d = inp()

print(findCapacity(weights,d))