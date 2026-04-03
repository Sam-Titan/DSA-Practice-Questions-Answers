# Brute Force Approach

def findthesum(nums, n):
    st = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets = tuple(sorted([nums[i], nums[j], nums[k]]))
                    st.add(triplets)
    return [triplets for triplets in st]

print("Brute Force Approach:")
print(findthesum([-1,0,1,2,-1,-4], 6))

# Better Approach

def findthesum(nums, n):
    st = set()
    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])
            if third in hashset:
                triplets = tuple(sorted([nums[i], nums[j], third]))
                st.add(triplets)
            hashset.add(nums[j])
    return [triplets for triplets in st]

print("Better Approach:")
print(findthesum([-1,0,1,2,-1,-4], 6))

# Optimal Approach

def findthesum(nums, n):
    nums.sort()
    result = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

print("Optimal Approach:")
print(findthesum([-1,0,1,2,-1,-4], 6))