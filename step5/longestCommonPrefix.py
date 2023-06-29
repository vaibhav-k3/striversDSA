
arr = [
    'hello',
    'world'
]


def longestCommonPrefix(arr):
    ans = ''
    max_length = 0
    i = 0
    length = 0
    while True:
        if i >= len(arr[0][i]):
            break
        char = arr[0][i]
        flag = 0
        for string in arr:
            if i >= len(string):
                flag = 1
                print("adsdasdasd")
            
            if char != string[i]:
                ans = ''
                max_length =0
        
        length+=1
        if length > max_length:
            max_length = length
            ans= ans+char
        if flag ==1:
            break
        i+=1
        
    print(ans)
    if ans == '':
        return -1
    else:
        ans
                

print(longestCommonPrefix(arr))