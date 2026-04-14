# Brute Force Approach

def maxProduct(nums):
    maxProd = nums[0]
    for i in range(len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            maxProd = max(maxProd, prod)
    return maxProd

print("Brute Force Approach")
print(maxProduct([2,3,-2,4]))

# Optimal Approach 1

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

print("Optimal Approach 1")
print(maxProduct([2,3,-2,4]))

# Optimal Approach 2

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

print("Optimal Approach 2")
print(maxProduct([2,3,-2,4]))