# Problem Description
# You are given a list of transactions, where each transaction is a list of products purchased together.
# [
# ['A','B','C'],
# ['A','B'],
# ['C','B'],
# ['A','B'],
# ['A','C']
# ]

# Task
# Return the pair of products that appears together most frequently across all transactions.

# Rules
# A pair consists of exactly two distinct products.
# (A, B) and (B, A) are considered the same pair.
# If multiple pairs have the same highest frequency, return the lexicographically smallest pair.

# Notes
# Duplicate items within a transaction should be counted only once.
# Each transaction can contribute multiple pairs.

# def pairs(nums):
#     hash_map = {}
#     n = len(nums)
#     my_set = [set(inner) for inner in nums]
#     my_list = [list(inner) for inner in my_set]
#     maxi = 0
#     for i in range(n):
#         my_list[i].sort()
#     for i in range(n):
#         for j in range(len(my_list[i]) - 1):
#             for e in range(len(my_list[i]) - 2):
#                 pair = my_list[i][j] + my_list[i][e]
#                 if pair in hash_map:
#                     hash_map[pair] = hash_map.get(pair, 0) + 1
#                 else:
#                     hash_map[pair] = hash_map.get(pair, 0) + 1

#     for i in range(len(hash_map)):
#         maxi = max(maxi, hash_map[i])

#     return maxi

# pairs([['A','B','C'],['A','B'],['C','B'],['A','B'],['A','C']])

from itertools import combinations

def pairs(nums):
    hash_map = {}

    # Step 1: Deduplicate within each transaction, then sort
    for transaction in nums:
        unique_items = sorted(set(transaction))

        # Step 2: Generate all valid pairs using combinations
        for pair in combinations(unique_items, 2):
            hash_map[pair] = hash_map.get(pair, 0) + 1

    # Step 3: Find max frequency
    maxi = max(hash_map.values())

    # Step 4: Collect all pairs with max frequency, return lexicographically smallest
    best = [pair for pair in hash_map if hash_map[pair] == maxi]

    return min(best)

print(pairs([['A','B','C'],['A','B'],['C','B'],['A','B'],['A','C']]))
# Output: ('A', 'B')