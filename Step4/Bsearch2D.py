


def binarySearch2d(matrix, key):
    n = len(matrix)
    m = len(matrix[0])
    # find lower bound of 0th column
    row_low = 0
    row_high = n - 1
    row = -1
    while row_low<=row_high:
        row = (row_low+row_high)//2
        if matrix[row][0] >= key:
            row_high = row - 1
        else:
            row_low = row + 1

    # found the right row
    # apply normal binary search of right row
    col_low = 0
    col_high = m -1 
    while col_low <= col_high:
        mid = (col_low+col_high)//2
        if matrix[row][mid] == key:
            return 1
        elif matrix[row][mid] < key:
            col_low = mid +1
        else:
            col_high = mid - 1

    return 0


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# TC : log(m) + log(n)
print(binarySearch2d(matrix,10))
