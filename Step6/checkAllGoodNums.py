from typing import List



def isGood(n,m,k):
    if n == 0:
        return True

    digit = n%10
    if digit == k:
        return False
    if digit > m or digit == 0:
        return isGood(n//10,digit+m,k)
    else:
        return False

def goodNumbers(a: int, b:int, digit:int) -> List[int]:
    ans = []
    for num in range(a,b+1):
        if isGood(num,0,digit):
            ans.append(num)
    
    return ans