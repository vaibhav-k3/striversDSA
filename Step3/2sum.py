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
hash = {}
for i in range(len(arr)):
    rem = k - arr[i]
    if rem in hash.keys():
        print(hash[rem],i)
        break
    else:
        hash[arr[i]] =i

