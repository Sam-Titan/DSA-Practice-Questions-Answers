# Brute Force Approach

def find_once(nums):
    n = len(nums)

    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count += 1
            if count == 1:
                return nums[i]
    return -1

print("Brute Force Method:")
print(find_once([1,2,2,3,4,3,4,5,6,5,6]))

# Better Approach

def find_once(nums):
    n = len(nums)
    # max1 = max(nums)
    # hash_map = [0] * int(max1 + 1)

    # for i in range(n):
    #     hash_map[nums[i]] += 1
    # for i in range(n):
    #     if hash_map[nums[i]] == 1:
    #         return nums[i]
    # return -1

    hash_map = {}
    for i in range(n):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

    for i in range(n):
        if hash_map[nums[i]] == 1:
            return nums[i]
        
    return -1

print("Better Approach:")
print(find_once([1,2,2,3,4,3,4,5,6,5,6]))

# Optimal Approach

def find_once(nums):
    xori = 0

    for num in nums:
        xori ^= num
    return xori

print("Optimal Approach:")
print(find_once([1,2,2,3,4,3,4,5,6,5,6]))