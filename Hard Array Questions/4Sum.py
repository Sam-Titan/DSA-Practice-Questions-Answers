# Brute Force Approach

def fourSum(nums, target):
    n = len(nums)
    st = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                        st.add(temp)
    return [quad for quad in st]

print("Brute Force Approach:")
print(fourSum([1,0,-1,0,-2,2], 0))

# Better Approach

def fourSum(nums, target):
    n = len(nums)
    st = set()
    for i in range(n):
        for j in range(i + 1, n):
            seen = set()
            for k in range(j + 1, n):
                required = target - nums[i] - nums[j] - nums[k]
                if required in seen:
                    temp = tuple(sorted([nums[i], nums[j], nums[k], required]))
                    st.add(temp)
                seen.add(nums[k])
    return [quad for quad in st]

print("Better Approach:")
print(fourSum([1,0,-1,0,-2,2], 0))

# Optimal Approach

def fourSum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result

print("Optimal Approach:")
print(fourSum([1,0,-1,0,-2,2], 0))