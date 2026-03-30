# Brute Force Approach

def rotate(matrix):
    m = len(matrix)
    temp = [[0] * m for i in range(m)]
    
    for i in range(m):
        for j in range(m):
            temp[j][m - i - 1] = matrix[i][j]
    for i in range(m):
        for j in range(m):
            matrix[i][j] = temp[i][j]
    return matrix

print("Brute Force Approach:")
print(rotate([[1,2,3], [4,5,6], [7,8,9]]))

# Optimal Approach

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix

print("Optimal Approach:")
print(rotate([[1,2,3], [4,5,6], [7,8,9]]))
