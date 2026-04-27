# Problem 4 — Two Sum II (Input Array Is Sorted) ⭐ (Easy)
# LeetCode 167

# Given a 1-indexed sorted array numbers, find two numbers that add up to target. Return their indices (1-indexed).

# Example:
# Input:  numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]
# Approach: Two pointers from opposite ends — sorted array means moving left right increases sum, moving right left decreases sum.

def twoSum(numbers, target):
    n = len(numbers)
    left, right = 0, n - 1
    
    while left < right:
        current = numbers[left] + numbers[right]
        if current == target:
            return [left + 1, right + 1]
        elif current > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]

print(twoSum([2, 7, 11, 15], 9))