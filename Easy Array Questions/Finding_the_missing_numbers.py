# Brute Force Method

def find_missing_number(nums):
    n = len(nums) + 1

    for i in range(1, n + 1):
        found = False
        for j in range(n - 1):
            if nums[j] == i:
                found = True
                break 
        if not found:
            return i
    return -1

print("Brute Force Approach:")
print(find_missing_number([1,2,3,4,5,6,7,8,10]))

# Better Approach

def find_missing_number(nums):
    n = len(nums) + 1
    hash_map = [0] * (n + 1)

    for i in range(n - 1):
        hash_map[nums[i]] += 1
    
    for j in range(1, n + 1):
        if hash_map[j] == 0:
            return j
    return -1

print("Better Approach:")
print(find_missing_number([1,2,3,4,5,6,7,8,10]))

# Expected Approach 1

def fing_missing_number(nums):
    n = len(nums)
    total = sum(nums)
    exp_total = n * (n - 1) // 2

    return exp_total - total

print("Expected Approach 1:")
print(find_missing_number([1,2,3,4,5,6,7,8,10]))

# Expected Approach 2

def find_missing_number(nums):
    n = len(nums) + 1
    xor1 = 0
    xor2 = 0

    for i in range(n - 1):
        xor2 ^= nums[i]

    for j in range(1, n + 1):
        xor1 ^= j

    return xor1 ^ xor2

print("Expected Approach 2:")
print(find_missing_number([1,2,3,4,5,6,7,8,10]))
