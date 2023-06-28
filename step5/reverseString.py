


def reverseString(string):
    i = 0 
    ans = ""
    cnt = 0
    temp = ""
    while i < len(string):
        if string[i]!=" ":
            temp+=string[i]
            
        elif string[i]==" ":
            if ans == "":
                ans = temp
            else:
                ans = temp + " " + ans
            temp = ""
        i+=1


    ans = temp + " " + ans
    return ans









string = input()
print(reverseString(string=string))