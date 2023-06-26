


def decompose(string):
    ans = ''
    cnt = 0
    i = 0
    while i < len(string):
        if string[i] == '(':
            cnt+=1
        
        if cnt > 1:
            ans=ans + string[i]

        if string[i] == ')':
            cnt-=1

        i+=1
    return ans





string = input()
print(decompose(string))