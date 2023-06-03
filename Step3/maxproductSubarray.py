def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


arr = inlt()
max_product = 0
product = 1
for num in arr:
    product = product * num
    max_product = max(product, max_product)
    if product == 0:
        product = 1

print(max_product)