def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def generateSubSeq(arr , i , n , ans,final):
    
    if i >=n:
        final.append(ans)
        return

    ans = ans + arr[i]
    generateSubSeq(arr,i+1,n,ans,final)
    ans = ans[:-1]
    generateSubSeq(arr,i+1,n,ans,final)


def distinct_sub_seq(str1 , str2):
    ans= ''
    ans1 = []
    generateSubSeq(str1 , 0 , len(str1) , ans,ans1)
    ans2 = []
    generateSubSeq(str2 , 0 , len(str2) , ans,ans2)

    ans1 = set(ans1)
    ans2 = set(ans2)

    if len(ans1) > len(ans2) :
        return str1
    else:
        return str2


str1 = input()
str2 = input()
print(distinct_sub_seq(str1,str2))





