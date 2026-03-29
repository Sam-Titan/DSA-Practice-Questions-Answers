# Brute Force Approach

def rearrange(nums, n):
    pos = []
    neg = []
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    for i in range(n//2):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]
    return nums

print("Brute Force Approach:")
print(rearrange([3,1,-2,-5,2,-4], 6))

# Optimal Approach

def rearrange(nums):
    n = len(nums)
    pos_index = 0
    neg_index = 1
    result =[0] * n
    for i in range(n):
        if nums[i] > 0:
            result[pos_index] = nums[i]
            pos_index += 2
        else:
            result[neg_index] = nums[i]
            neg_index += 2
    return result

print("Optimal Approach:")
print(rearrange([3,1,-2,-5,2,-4]))