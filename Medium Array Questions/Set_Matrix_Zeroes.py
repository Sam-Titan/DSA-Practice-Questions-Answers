# Brute Force Approach

def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                for row in range(m):
                    if matrix[row][j] != 0:
                        matrix[row][j] = -1
                for col in range(n):
                    if matrix[i][col] != 0:
                        matrix[i][col] = -1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix

print("Brute Force Approach:")
print(setZeroes([[1,2,3], [0,1,2], [1,2,0]]))

# Better Approach

def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = [0] * m
    col = [0] * n
    for i in range(m):
        for j in range(n):
           if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(m):
        for j in range(n):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0
    return matrix

print("Better Approach:")
print(setZeroes([[1,2,3], [0,1,2], [1,2,0]]))

# Optimal Approach

def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    first_row_zeroes = False
    first_col_zeroes = False

    for i in range(m):
        if matrix[i][0] == 0:
            first_row_zeroes = True
            break

    for j in range(n):
        if matrix[0][j] == 0:
            first_col_zeroes = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_zeroes:
        for i in range(m):
            matrix[i][0] = 0

    if first_col_zeroes:
        for j in range(n):
            matrix[0][j] = 0 

    return matrix

print("Optimal Approach:")
print(setZeroes([[1,2,3], [0,1,2], [1,2,0]]))
