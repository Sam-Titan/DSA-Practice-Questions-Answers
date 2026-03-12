# Count the number of digits present in a number N

# import math

# N = 1234

# cnt = int(math.log10(N) + 1)

# print(cnt)



# Reverse the Number

# class Solution:
#     def reverse(self, x: int) -> int:
#         if x > (2^31 -1) or x < -2^31:
#             return 0
#         a = 0
#         check = True
#         if x < 0:
#             check = False
#             x = x * -1

#         while x > 0:
#             n = x % 10
#             a = a*10 + n
#             x = x // 10
        
#         if check == False:
#             a = a * -1
#         return a

# print(Solution().reverse(123456789))

a = 20
b = 15

while a > 0 and b > 0:
    if a > b:
        a = a % b
    else:
        b = b % a

if a == 0:
    print(b)
else:
    print(a)