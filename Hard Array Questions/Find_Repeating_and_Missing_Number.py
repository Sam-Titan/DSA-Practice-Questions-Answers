# Brute Force Approach

def findMissingRepeatingNumbers(nums):
    n = len(nums)
    repeating = -1
    missing = -1
    for i in range(1, n + 1):
        cnt = nums.count(i)
        if cnt == 2:
            repeating = i
        elif cnt == 0:
            missing = i
        if repeating != -1 and missing != -1:
            break
    return[repeating, missing]

print("Brute Force Approach:")
print(findMissingRepeatingNumbers([1,2,2,3,4,5]))

# Better Approach

def findMissingRepeatingNumbers(nums):
    n = len(nums)
    hash_map = [0] * (n + 1)
    for num in nums:
        hash_map[num] += 1
    repeating = -1
    missing = -1
    for i in range(1, n + 1):
        if hash_map[i] == 2:
            repeating = i
        elif hash_map[i] == 0:
            missing = i
        if repeating != -1 and missing != -1:
            break
    return[repeating, missing]

print("Brute Force Approach:")
print(findMissingRepeatingNumbers([1,2,2,3,4,5]))

# Optimal Approach 1

def findMissingRepeatingNumbers(nums):
    n = len(nums)
    SN = (n * (n + 1)) // 2
    S2N = (n * (n + 1) * (2 * n + 1)) // 6
    
    S = 0
    S2 = 0
    for num in nums:
        S += num
        S2 += num * num

    val1 = S - SN
    val2 = S2 - S2N
    val2 = val2 // val1
    x = (val1 + val2) // 2
    y = x - val1
    return [int(x), int(y)]

print("Optimal Approach 1:")
print(findMissingRepeatingNumbers([1,2,2,3,4,5]))

# Optimal Approach 2

def findMissingRepeatingNumbers(nums):
    n = len(nums)
    xr = 0
    for i in range(n):
        xr = xr ^ nums[i]
        xr = xr ^ (i + 1)
    number = (xr & ~(xr - 1))
    zero = 0
    one = 0 
    for i in range(n):
        if (nums[i] & number) != 0:
            one = one ^ nums[i]
        else:
            zero = zero ^ nums[i]
    for i in range(1, n + 1):
        if (i & number) != 0:
            one = one ^ i
        else:
            zero = zero ^ i
    cnt = 0
    for i in range(n):
        if nums[i] == zero:
            cnt += 1
    if cnt == 2:
        return [zero, one]
    else:
        return [one, zero]
    
print("Optimal Approach 2:")
print(findMissingRepeatingNumbers([1,2,2,3,4,5]))