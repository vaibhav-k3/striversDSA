def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


matrix = [[1,2,3,10],
          [4,5,6,11],
          [7,8,9,12]]

row = 0
col = 0
cnt = 0
while cnt < len(matrix) * len(matrix[0]):
    itr = 0
    while col < len(matrix[0]) - itr and cnt < len(matrix) * len(matrix[0]):
        print(matrix[row][col])
        col+=1
        cnt+=1
    col-=1
    row+=1
    while row < len(matrix) - itr and cnt < len(matrix) * len(matrix[0]):
        print(matrix[row][col])
        row+=1
        cnt+=1
    
    col-=1
    row-=1
    while col >=0+itr and cnt < len(matrix) * len(matrix[0]):
        print(matrix[row][col])
        col-=1
        cnt+=1
    
    col+=1
    row-=1
    while row > 0+itr and cnt < len(matrix) * len(matrix[0]):
        print(matrix[row][col])
        row-=1
        cnt+=1
    row=+1
    itr+=1
    col+=1


