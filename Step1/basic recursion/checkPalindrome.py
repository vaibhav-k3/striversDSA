def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def checkPalindrome(arr,i,n):
    if i < n//2:
        return True

    if arr[i] == arr[n-i-1]:
        return checkPalindrome(arr,i-1,n)
    else:
        return False



arr = insr()
n = len(arr)
ans = checkPalindrome(arr,n-1,n)
print(ans)