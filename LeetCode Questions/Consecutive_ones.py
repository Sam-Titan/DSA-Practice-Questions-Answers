# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

def findMaxConsecutiveOnes(nums):
    total = 0
    max_total = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            total += 1
        else:
            if total > max_total:
                max_total = total
            total = 0
    if total > max_total:
        max_total = total

    return max_total

print(findMaxConsecutiveOnes([1,1,0,1,1,0,1,1,1]))

