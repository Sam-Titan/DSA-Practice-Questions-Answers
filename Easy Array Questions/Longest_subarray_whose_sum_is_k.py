# Brute Force Approach

def longest_subarray(nums, k):
    n = len(nums)
    max_length = 0

    for i in range(n):
        for j in range(i, n):
            current = 0
            for a in range(i, j + 1):
                current += nums[a]
            if current == k:
                max_length = max(max_length, j - i + 1)
    return max_length

print("Brute Force Method:")
print(longest_subarray([1,2,3,4,5], 5))

# Optimal Method

def longest_subarray(nums, k):
    n = len(nums)
    max_length = 0

    left = 0
    right = 0

    s = nums[0]

    while right < n:
        if left <= right and s > k:
            s -= nums[left]
            left += 1
        if s == k:
            max_length = max(max_length, right - left + 1)

        right += 1
        if right < n:
            s += nums[right]
    return max_length

print("Optimal Approach:")
print(longest_subarray([1,2,3,4,5], 5))