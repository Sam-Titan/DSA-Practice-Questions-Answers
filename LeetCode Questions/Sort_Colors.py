# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

# My Method

def sortcolors(nums):
    n = len(nums)
    hash_map = {0 : 0, 1 : 0, 2 : 0}

    for i in range(n):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
    
    current_index = 0
    for i in range(3):
        for j in range(hash_map[i]):
            nums[current_index] = i
            current_index += 1
    return nums

print("Using Hash Map:")
print(sortcolors([1,1,2,2,0,0]))

# Optimal Method

def sortcolors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low] , nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

print("Optimal Approach/ Butch National Flag Algorithm:")
print(sortcolors([1,1,2,2,0,0]))
