# Brute Force Approach

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]

print("Brute Force Approach:")
print(twoSum([1,2,3,4,5], 5))

# Better Approach

def twoSum(nums, target):
    n = len(nums)
    hash_map = {}
    for i in range(n):
        compliment = target - nums[i]
        if compliment in hash_map:
            return [hash_map[compliment], i]
        hash_map[nums[i]] = i
    return [-1, -1]

print("Better Approach:")
print(twoSum([1,2,3,4,5], 5))

# Optimal Approach

def twoSum(nums, target):
    nums_with_index = [(num, idx) for idx, num in enumerate(nums)]
    nums_with_index.sort()
    right, left = 0, len(nums) - 1
    while right < left:
        current_sum = nums_with_index[right][0] + nums_with_index[left][0]
        if current_sum == target:
            return (nums_with_index[right][1], nums_with_index[left][1])
        elif current_sum < target:
            right += 1
        else:
           left -= 1
    return [-1, -1]

print("Optimal Approach:")
print(twoSum([1,2,3,4,5], 5))