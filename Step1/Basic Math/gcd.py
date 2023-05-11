def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))



def gcd(a,b):
    if b == 0:
        return a
    
    return gcd(b,a%b)

n1 = inp()
n2 = inp()

print(gcd(n1,n2))


