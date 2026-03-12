n = 5

# for i in range(n):
#     for j in range(n):
#         print("*"*2, end="")
#     print("\n")

# i = 0
# while i != n:
#     i += 1
#     for j in range(i):
#         print("*", end="")
#     print()

# i = 0
# while i != n:
#     i += 1
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# for i in range(1, n + 1):
#     print(f"{i}"*i)

# for i in range(n, 0, -1):
#     print("*"*i)

# while n > 0:
#     for i in range(1, n + 1):
#         print(i, end="")
#     print()
#     n -= 1

# j = 1
# for i in range(1, n + 1):
#     print(" " * (n - i), end = "")
#     print("*" * j)
#     j += 2
    
# j = (n * 2) - 1
# for i in range(n, 0, -1):
#     print(" " * (n - i), end = "")
#     print("*" * j)
#     j -= 2

# class Solution:
#     def pattern10(self, n):
#         i = 0
#         a = n * 2
#         while i < n * 2:
#             i += 1
#             a -= 1
#             if i <= n:
#                 for j in range(i):
#                     print("*", end="")
#                 print()
#             else:
#                 for k in range(a, 0, -1):
#                     print("*", end="")
#                 print()
# Solution().pattern10(5)

# class Solution:
#     def pattern11(self, n):
#         i = 0
#         while i < n:
#             i += 1
#             for j in range(i, 0, -1):
#                 print(j%2, end="")
#             print()
            
# Solution().pattern11(5)

# class Solution:
#     def pattern12(self, n):
#         i = 0
#         while i < n:
#             i += 1
#             for j in range(1, i + 1):
#                 print(j, end="")
#             print(" "*(n*2-i*2), end="")
#             for j in range(i, 0, -1):
#                 print(j, end="")
#             print()
# Solution().pattern12(5)

class Solution:
    def pattern21(self, n):
        print("*"*n)
        for i in range(1, n-1):
            print("*", end="")
            print(" "*(n-2), end="")
            print("*", end="")
            print()
        print("*"*n)
Solution().pattern21(5)