# Algorithm 1

def PascalTriangle(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

print("Algorithm 1:")
print(PascalTriangle(5))

# Algorithm 2

def findNRow(N):
    row = []
    val = 1
    row.append(val)
    for i in range(1, N):
        val = val * (N - i) // i
        row.append(val)
    return row

print("Algorithm 2:")
print(findNRow(5))

# Algorithm 3

def findPascalElement(r, c):
    n = r - 1
    k = c - 1
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

print("Algorithm 3:")
print(findPascalElement(5, 3))
