def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


n = inp()
reverse = 0 
while n > 0:
    digit = n % 10
    reverse = reverse*10 + digit
    n//=10

print(reverse)
