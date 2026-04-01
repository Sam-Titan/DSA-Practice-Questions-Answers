# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow up: Could you solve the problem in linear time and in O(1) space?


# My try 

def majorityElement(nums):
    n = len(nums)
    hash_map = {}
    max_ele = []
    for i in range(n):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
        if hash_map[nums[i]] > (n // 3) and nums[i] not in max_ele:
            max_ele.append(nums[i])
    return max_ele

print(majorityElement([1,2,1,2,3]))
