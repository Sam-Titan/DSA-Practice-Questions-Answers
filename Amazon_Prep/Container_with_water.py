# Problem 5 — Container With Most Water ⭐⭐ (Medium)
# LeetCode 11

# Given an array height where height[i] is the height of a vertical line at index i, find two lines that together with the x-axis forms a container that holds the most water.

# Example:
# Input:  height = [1,8,6,2,5,4,8,3,7]
# Output: 49

def maxArea(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        current_area = width * min(height[right], height[left])
        best = max(best, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

print(maxArea([1,8,6,2,5,4,8,3,7]))