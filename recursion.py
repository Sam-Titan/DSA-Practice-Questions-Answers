# n = 10
# Current = 1
# # Forward Recursion
# def printnumbers(Current, n):
#     if Current > n:
#         return
    
#     print(Current, end =" ")

#     printnumbers(Current + 1, n)    
    
# printnumbers(Current, n)
# print()

# # Backtracking
# def printnumbers(Current, n):
#     if Current > n:
#         return
    
#     printnumbers(Current + 1, n)

#     print(Current, end =" ")

# printnumbers(Current, n)



# Sum of N nunbers

# N = 5
# def sumofnumbers(N):
#     if N == 1:
#         return 1
    
#     return N + sumofnumbers(N - 1)

# print(sumofnumbers(N))

# Factorial of N

# N = 5 
# def printfactorial(N):
#     if N == 1:
#         return 1
#     return N * printfactorial(N - 1)

# print(printfactorial(N))

# import re

# def palindrome(s):
#     cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
#     for i in range(len(cleaned) // 2):
#         if cleaned[i] != cleaned[len(cleaned) - 1 - i]:
#             return False
#     return True

# print(palindrome("A man, a plan, a canal: Panama"))

# def palindrome(s):
#     s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
#     p1 = 0
#     p2 = len(s) - 1
#     while p1 < p2:
#         if s[p1] == s[p2]:
#             p1 += 1
#             p2 -= 1
#         else:
#             return False
#     return True

# print(palindrome("Panama"))


def fibonacci(N):
    # Base case: if N is 0 or 1, return N
    if N <= 1:
        return N

    # Recursive calls: calculate previous two terms
    last = fibonacci(N - 1)   # (N-1)th term
    slast = fibonacci(N - 2)  # (N-2)th term

    return last + slast

# Driver code
N = 4
print(fibonacci(N))  # Output: 3
