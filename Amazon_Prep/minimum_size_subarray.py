# Problem 3 — Minimum Size Subarray Sum ⭐⭐ (Medium)
# LeetCode 209

# Given an array of positive integers nums and a positive integer target, return the minimum length of a contiguous subarray whose sum is ≥ target. Return 0 if no such subarray exists.

# Example:
# Input:  nums = [2,3,1,2,4,3], target = 7
# Output: 2   ← [4,3]

def minimumsubarray(nums, target):
    left = 0
    Current_sum = 0
    best = float("inf")
    for right in range(len(nums)):
        Current_sum += nums[right]
        while Current_sum >= target:
            best = min(best, right - left + 1)
            Current_sum -= nums[left]
            left += 1
    return best if best != float("inf") else 0

print(minimumsubarray([2,3,1,2,4,3], 7))