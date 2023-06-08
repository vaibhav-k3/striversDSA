def solution(matrix):
    # Type your solution here
    n = len(matrix)
    m = len(matrix[0])
    temp = [0*m]*n
    for i in range(0,n):
        for j in range(0,m):
            temp[j][i]=matrix[i][j]
            print(i,j)
            print(temp)
    
    for i in range(n):
        print(temp[i])
    
    return temp


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(solution(matrix=matrix))