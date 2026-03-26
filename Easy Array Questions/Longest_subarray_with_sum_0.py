# Brute Force Approach

def longest_subarray(nums):
    max_len = 0
    hash_map = {}
    s = 0
    for i, val in enumerate(nums):
        s += val
        if s == 0:
            max_len = i + 1
        elif s in hash_map:
            max_len = max(max_len, i - hash_map[s])
        else:
            hash_map[s] = i

    return max_len

print("Brute Force Method:")
print(longest_subarray([1,2,3,-1,-2]))

# Optimal Approach

def longest_subarray(nums, n):
    hash_map = {}
    max_len = 0
    s = 0
    for i in range(n):
        s += nums[i]
        if s == 0:
            max_len = i + 1
        else:
            if s in hash_map:
                max_len = max(max_len, i - hash_map[s])
            else:
                hash_map[s] = i

    return max_len

print("Optimal Approach:")
print(longest_subarray([1,2,3,-1,-2], 5))
