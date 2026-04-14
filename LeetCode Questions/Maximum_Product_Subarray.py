# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.


def maxProduct(nums):
    n = len(nums)
    pre, suff = 1, 1
    ans = float("-inf")

    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= nums[i]
        suff *= nums[n - i - 1]
        ans = max(ans, pre, suff)
    return ans

print(maxProduct([2,3,-2,4]))

def maxProduct(nums):
    res = nums[0]
    maxProd = nums[0]
    minProd = nums[0]
    for i in range(1, len(nums)):
        curr = nums[i]
        if curr < 0:
            maxProd, minProd = minProd, maxProd
        maxProd = max(curr, maxProd * curr)
        minProd = min(curr, minProd * curr)
        res = max(res, maxProd)
    return res

print(maxProduct([2,3,-2,4]))