# Pattern D: Existence Check (Has this been seen before?)
# Problem type: Find first duplicate, detect if a value exists, check intersection.

def check(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(check([1,2,3,4,5,1]))

# Input:  nums = [1, 2, 3, 1]
# Output: True

print(check([1, 2, 3, 1]))

def check(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = seen.get(num, 0) + 1
    return False

print(check([1,2,3,4,5,1]))

# Input:  nums = [1, 2, 3, 1]
# Output: True

print(check([1, 2, 3, 1]))