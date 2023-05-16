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
max_profit = -1
buy = arr[0]
for i in range(1,len(arr)):
    buy = min(arr[i],buy)
    profit = arr[i] - buy
    max_profit = max(max_profit,profit)
    
print(max_profit)