# Brute Force Approach

def majorityElement(nums):
    n = len(nums)

    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count += 1
        if count > (n // 2):
            return nums[i]
    return -1

print("Brute Force Approach:")
print(majorityElement([1,2,2,1,2]))

# Better Approach

def majorityElement(nums):
    n = len(nums)
    hash_map = {}
    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1
        
    for key, value in hash_map.items():
        if value > (n // 2):
            return key
    return -1

print("Better Approach:")
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