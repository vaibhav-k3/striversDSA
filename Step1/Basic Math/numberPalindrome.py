def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

#approach 1
n = inp()
# digits = []
# while n > 0:
#     digits.append(n%10)
#     n//=10

# flag = True
# for i in range(len(digits)//2):
#     if digits[i]!=digits[len(digits)-i-1]:
#         flag = False

# if flag:
#     print("palindrom")
# else:
#     print("not a palindrome")
reverse = 0
x = n
while n>0:
    reverse = reverse*10 + n%10
    n//=10

if x == reverse:
    print("palindrom")
else:
     print("not a palindrome")