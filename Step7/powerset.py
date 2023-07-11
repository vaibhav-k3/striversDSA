def inlt():
    return(list(map(int,input().split())))


arr = inlt()
ans = []

def powerset(arr , i , n , ans):
    if i>=n:
        print(ans)
    else:
        ans.append(arr[i])
        powerset(arr,i+1,n,ans)
        ans.pop(-1)
        powerset(arr,i+1,n,ans)
powerset(arr,0,len(arr),ans)