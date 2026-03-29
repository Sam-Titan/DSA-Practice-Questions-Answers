# Brute Foce Approach

def linear_Search(nums, num):
    n = len(nums)
    for i in range(n):
        if nums[i] == num:
            return True
    return False

def longestConsecutive(nums):
    n = len(nums)
    if n == 0:
        return 0
    longest = 0
    for i in range(n):
        cnt = 1
        x = nums[i]
        while linear_Search(nums, x + 1):
            cnt += 1
            x += 1
        longest = max(longest, cnt)
    return longest

print("Brute Force Approach:")
print(longestConsecutive([100, 4, 200, 1, 3, 2]))

# Better Approach

def longestConsecutive(nums):
    n = len(nums)
    if n == 0:
        return 0
    nums.sort()
    longest = 0
    lastSmaller = float("-inf")
    cnt = 1
    for i in range(n):
        if nums[i] - 1 == lastSmaller:
            cnt += 1
            lastSmaller = nums[i]
        elif nums[i] != lastSmaller:
            cnt = 1
            lastSmaller = nums[i]
        longest = max(longest, cnt)
    return longest

print("Better Approach:")
print(longestConsecutive([100, 4, 200, 1, 3, 2]))

# Optimal Approach

def longestConsecutive(nums):
    n = len(nums)
    if n == 0:
        return 0
    longest = 1
    st = set()
    for i in range(n):
        st.add(nums[i])
    for it in st:
        if it - 1 not in st:
            cnt = 1
            x = it
            while x + 1 in st:
                x = x + 1
                cnt = cnt + 1
            longest = max(longest, cnt)
    return longest

print("Optimal Approach:")
print(longestConsecutive([100, 4, 200, 1, 3, 2]))