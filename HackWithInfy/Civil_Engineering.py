# Problem Statement

# Alice, a civil engineer, is designing a grand staircase using exactly N stone blocks.

# To make the staircase aesthetically pleasing, Alice has the following strict rules:

# The staircase must have at least 2 steps.
# Each ascending step must contain exactly one more block than the previous step.
# Example: if the first step has 3 blocks, the next must have 4, then 5, and so on.
# All N blocks must be used.
# Task

# Given the number of blocks N, determine whether it is possible to build a staircase that satisfies all the above rules.

# Input Format
# The input contains a single integer N, representing the total number of stone blocks.
# Output Format
# Print "YES" if it is possible to build the staircase.
# Otherwise, print "NO".
# Example

# Input:

# 3

# Output:

# YES

# Explanation:

# We can build a staircase with 2 steps:

# Step 1 → 1 block
# Step 2 → 2 blocks

# Total = 3 blocks 

# My Approach
# 1 + 2 + .... + N\
# Sum = (N * (N + 1)) // 2
# N = (-b + sqrt(b^2 + 4ac)) // 2a
# N = (-1 + sqrt(1 + 8*S)) // 2


def civil_engineering(S):
    N = int((-1 + ((1 + 8*S) ** 0.5)) / 2)

    if S == (N * (N + 1)) // 2:
        return "YES"
    else:
        return "NO"

S = int(input("Enter the number of Blocks:"))

if S > 2:
    print(civil_engineering(S))
else:
    print("NO")

# ChatGPT Approach

def civil_engineering(S):
    if S <= 2:
        return "NO"
    
    # Check if power of 2
    if (S & (S - 1)) == 0:
        return "NO"
    
    return "YES"

S = int(input("Enter the number of Blocks:"))
print(civil_engineering(S))