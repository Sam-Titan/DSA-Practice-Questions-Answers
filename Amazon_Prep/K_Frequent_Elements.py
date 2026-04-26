# LeetCode 347

# Given an integer array nums and an integer k, return the k most frequent elements.

# Example:
# Input:  nums = [1,1,1,2,2,3], k = 2
# Output: [1, 2]

from collections import Counter

def K_frequent_elements(nums, k):
    freq = Counter(nums)
    return[item for item, count in freq.most_common(k)]

print(K_frequent_elements([1,1,1,2,2,3], 2))