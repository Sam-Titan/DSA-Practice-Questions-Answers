# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# The input is generated such that a majority element will exist in the array.
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?

# My solution

def majorityElement(nums):
    n = len(nums)
    hash_map = {}
    for i in range(n):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
    for key, value in hash_map.items():
        if value > (n // 2):
            return key
    return -1

print("My Approach:")
print(majorityElement([1,2,2,1,2]))

# Optimal Approach

def majorityElement(nums):
    n = len(nums)
    cnt = 0
    el = 0
    for num in nums:
        if cnt == 0:
            cnt = 1
            el = num
        elif el == num:
            cnt += 1
        else:
            cnt -= 1
    cnt = nums.count(el)

    if cnt > (n // 2):
        return el
    return -1

print("Optimal Approach:")
print(majorityElement([1,2,2,1,2]))