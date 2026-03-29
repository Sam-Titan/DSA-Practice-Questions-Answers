# Brute Force Approach

from itertools import permutations

def nextPermutation(nums):
    perms = sorted(set(permutations(nums)))
    current = tuple(nums)

    for i in range(len(perms)):
        if perms[i] == current:
            if i == len(perms) - 1:
                return list(perms[0])
            return list(perms[i + 1])
    return nums

print("Brute Force Approach:")
print(nextPermutation([1,2,3]))

# Optimal Approach

def nextPermutation(nums):
    index = -1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            index = i
            break
    if index == -1:
        nums.reverse()
        return
    
    for i in range(len(nums) - 1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break
    nums[index + 1:] = reversed(nums[index + 1:])
    return nums

print("Optimal Approach:")
print(nextPermutation([1,2,3]))