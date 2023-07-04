from collections import defaultdict



def sortString(string):
    sorted_string = ''
    freq = defaultdict(int)
    for char in string:
        if char != ' ':
            freq[char]+=1
    
    freq = sorted(freq.items(), key= lambda x:x[1],reverse=True)
    
    for k in freq:
        for _ in range(k[1]):
            sorted_string = sorted_string + k[0] + ' '

    return sorted_string



print(sortString('4 2 5 5 5'))
