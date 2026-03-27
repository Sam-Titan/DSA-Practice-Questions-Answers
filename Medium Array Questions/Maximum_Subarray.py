# Optimal Approach

def maxSubArray(nums):
    count = 0
    max1 = float('-inf')
    for num in nums:
        count += num
        if max1 < count:
            max1 = count
        if count < 0:
            count = 0
    return max1

print("Optimal Approach:")
print(maxSubArray([1,-1,2,3,-2]))

# Follow Up

def maxSubArray(nums):
    count = 0
    max1 = float('-inf')
    start = 0
    ansStart = -1
    ansEnd = -1
    for i in range(len(nums)):
        if count == 0:
            start = i
        count += nums[i]
        if max1 < count:
            max1 = count
            ansStart = start
            ansEnd = i
        if count < 0:
            count = 0
    print("The Maximum Subarray:", end="")
    for i in range(ansStart, ansEnd + 1):
        print(nums[i], end=" ")
    print()
    return max1

print("Follow Up:")
print(maxSubArray([1,-1,2,3,-2]))