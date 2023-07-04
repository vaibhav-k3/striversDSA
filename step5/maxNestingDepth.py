

def maxNestingDepth(string):
    maxDepth = 0
    cnt = 0
    for char in string:
        if char == "(":
            cnt+=1
        elif char == ")":
            cnt-=1

        maxDepth = max(maxDepth,cnt)

    return maxDepth


print(maxNestingDepth("(9+0 + (9))"))