# Brute Force Approach

def leaders(nums):
    ans = []
    for i in range(len(nums)):
        leader = True
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                leader = False
                break
        if leader:
            ans.append(nums[i])
    return ans

print("Brute Force Approach:")
print(leaders([10, 22, 12, 3, 0, 6]))

# Optimal Approach

def leaders(nums):
    ans = []
    if not nums:
        return ans
    
    max_value = nums[-1]
    ans.append(nums[-1])
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] > max_value:
            ans.append(nums[i])
            max_value = nums[i]
    ans.reverse()
    return ans

print("Optimal Approach:")
print(leaders([10, 22, 12, 3, 0, 6]))