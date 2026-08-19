# B. Evanescent
# time limit per test2 seconds
# memory limit per test256 megabytes
# Let f(s)
#  be the compressed version of a string s
# , formed by replacing every maximal contiguous block of identical characters with a single copy of that character. For example, f(
# "aabbcc") = 
# "abc".

# Let |s|
#  denote the length of a string s
# . Following this, |f(s)|
#  denotes the length of the compressed string. For example:

# |f(
# "aabbcc")|=
#  |
# "abc"|
#  =3
# If the string is empty, its length is 0
# .
# Yousef has given you a string s
#  consisting of n
#  lowercase Latin letters. You must delete exactly one character si
#  (2≤i≤n−1
# ) to form a new string s′
# , and then find the minimum possible value of |f(s′)|
# .

# Note that you cannot delete s1
#  or sn
# .

# Input
# The first line contains an integer t
#  (1≤t≤104
# ) — the number of test cases.

# The first line of each test case contains an integer n
#  (3≤n≤2⋅105
# ) — the length of the string.

# The second line of each test case contains a string s
#  (|s|=n
# ), consisting of lowercase Latin letters.

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output a single integer — the minimum possible length of the resulting compressed string after deleting one character.

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    base = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            base += 1
    max_reduction = 0

    for i in range(1, n - 1):
        if s[i-1] != s[i] and s[i] != s[i + 1]:
            if s[i - 1] == s[i + 1]:
                max_reduction = max(max_reduction, 2)
            else:
                max_reduction = max(max_reduction, 1)
    print(base - max_reduction)