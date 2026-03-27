# My Method

def sortcolors(nums):
    n = len(nums)
    hash_map = {0 : 0, 1 : 0, 2 : 0}

    for i in range(n):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
    
    current_index = 0
    for i in range(3):
        for j in range(hash_map[i]):
            nums[current_index] = i
            current_index += 1
    return nums

print("Using Hash Map:")
print(sortcolors([1,1,2,2,0,0]))

# Optimal Method

def sortcolors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low] , nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

print("Optimal Approach/ Butch National Flag Algorithm:")
print(sortcolors([1,1,2,2,0,0]))
