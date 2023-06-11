
def getUpperBound(row, key):
    low = 0
    high = len(row) - 1
    while low <= high:
        mid = (low+high)//2
        if row[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1
    
    return low




def matrixMedian(matrix):
    
    n = len(matrix)
    m = len(matrix[0])

    low = 1
    high = 1000000
    while low <= high:
        mid = (low+high)//2
        cnt = 0
        for row in matrix:
            cnt = cnt + getUpperBound(row, mid)
        
        # if cnt == (n*m)//2 - 1:
        #     return mid

        if cnt <=(n*m)//2 -1:
            low = mid + 1
        else:
            high = mid - 1
    
    return low + 1


matrix = [
    [1, 4 ,9],
    [2,5,6],
    [3,8,7]
]
print(matrixMedian(matrix))

# 1 1 2 3 5 6 7 8 9