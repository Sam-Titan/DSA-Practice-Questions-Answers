# Brute Force Approach

def majorityElement(nums):
    n = len(nums)
    result = []
    for i in range(n):
        if len(result) == 0 or result[0] != nums[i]:
            count = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1
            if count > n // 3:
                result.append(nums[i])
        if len(result) == 2:
                break
    return result

print("Brute Force Approach:")
print(majorityElement([1,2,1,2,3]))

# Better Approach
from collections import defaultdict

def majorityElement(nums):
    n = len(nums)
    hash_map = defaultdict(int)
    majority = n // 3 + 1
    result = []
    for num in nums:
        hash_map[num] += 1
        if hash_map[num] == majority:
            result.append(num)
        if len(result) == 2:
            break
    return result

print("Better Approach:")
print(majorityElement([1,2,1,2,3]))

# Optimal Approach

def majorityElement(nums):
    n = len(nums)
    cnt1, cnt2 = 0, 0
    ele1, ele2 = float("-inf"), float("-inf")
    for num in nums:
        if cnt1 == 0 and ele2 != num:
            cnt1 = 1
            ele1 = num
        elif cnt2 == 0 and ele1 != num:
            cnt2 = 1
            ele2 = num
        elif ele1 == num:
            cnt1 += 1
        elif ele2 == num:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    cnt1, cnt2 = 0, 0
    for num in nums:
        if num == ele1:
            cnt1 += 1
        if num == ele2:
            cnt2 += 1
    mini = (n // 3) + 1
    result = []
    if cnt1 >= mini:
        result.append(ele1)
    if cnt2 >= mini and ele1 != ele2:
        result.append(ele2)
    return result

print("Optimal Approach:")
print(majorityElement([1,2,1,2,3]))
