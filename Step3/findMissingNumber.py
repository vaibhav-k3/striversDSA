def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

arr1 = inlt()
sum = 0
max_number = arr1[-1]
for num in arr1:
    sum+=num

desired_sum = max_number*(max_number+1)//2
missing = desired_sum - sum
print(missing)