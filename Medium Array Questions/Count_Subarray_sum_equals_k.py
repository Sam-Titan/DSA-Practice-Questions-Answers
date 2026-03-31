# Brute Force Approach

def subarraySum(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            total = 0
            for m in range(i, j + 1):
                total += nums[m]
            if total == k:
                count += 1
    return count

print("Brute Force Approach:")
print(subarraySum([1,1,1], 2))

# Better Approach

def subarraySum(nums, k):
    n = len(nums)
    total = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if s == k:
                total += 1
    return total

print("Better Approach:")
print(subarraySum([1,1,1], 2))

# Optimal Approach

def subarraySum(nums, k):
    n = len(nums)
    prefixSumCount = {}
    prefixSum = 0
    count = 0
    prefixSumCount[0] = 1
    for i in range(n):
        prefixSum += nums[i]
        remove = prefixSum - k
        if remove in prefixSumCount:
            count += prefixSumCount[remove]
        prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1
    return count

print("Optimal Approach:")
print(subarraySum([1,1,1], 2))
