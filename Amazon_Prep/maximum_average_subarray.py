# Problem 1 — Maximum Average Subarray I ⭐ (Easy)
# LeetCode 643

# Given an integer array nums and integer k, find the contiguous subarray of length k with the maximum average. Return the maximum average.

# Example:
# Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75
# Explanation: [12, -5, -6, 50] → sum = 51 → avg = 51/4 = 12.75
# Approach: Fixed sliding window — maximize sum, divide by k at the end.

def subarray(nums, k):
    s = sum(nums[:k])
    best = s
    for i in range(k, len(nums)):
        s += nums[i]
        s -= nums[i - k]
        best = max(best, s)
    return float(best)/float(k)

print(subarray([1, 12, -5, -6, 50, 3], 4))