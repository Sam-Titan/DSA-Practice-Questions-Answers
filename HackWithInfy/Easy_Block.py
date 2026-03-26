# N, A, B 
# Example: 3, [2, 1, 2], [1, 2, 2]
# A will represent 1
# B will represent 0
# No adjacent blocks can be present, A[0] and A[1] can't be adjacent instead A[0] and B[0] can be.
# Output should 1101100100

def binary(N, A, B):
    Mod = 10**9 + 7
    B.sort()
    A.sort(reverse = True)
    result = 0
    for i in range(N):
        for _ in range(A[i]):
            result = (result * 2 + 1) % Mod
        for _ in range(B[i]):
            result = (result * 2) % Mod

    print(result)
    return result

print(binary(2, [2, 1], [1, 2]))