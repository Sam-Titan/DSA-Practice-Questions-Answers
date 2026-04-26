# Given an array, find two elements that satisfy a condition (sum to target, differ by k, etc.)

def find(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        required = target - num
        if required in seen:
            return [seen[required], i]
        seen[num] = i
    return [-1, -1]

print(find([1,2,3,4,5], 3))

# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]   ← because nums[0] + nums[1] = 2 + 7 = 9

print(find([2, 7, 11, 15], 9))

# differ by k

def find(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen:
            return [seen[num], i]  
        required = target + num
        if required not in seen:
            seen[required] = i
    return [-1, -1]

print(find([1,2,3,4,5], 3))

# Better way 

def find(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if num - target in seen:
            return [seen[num - target], i] 
        if num + target in seen:
            return [seen[num + target], i]  
        seen[num] = i
    return [-1, -1]

print(find([1,2,3,4,5], 3))

def find(nums, target):
    seen = set(nums)
    for num in nums:
        if num + target in seen:
            return [num, num + target]
    return []

print(find([1,2,3,1,4,5], 3))