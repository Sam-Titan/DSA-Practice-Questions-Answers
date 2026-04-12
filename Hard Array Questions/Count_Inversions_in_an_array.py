# Brute Force Approach

def number_of_inversions(nums):
    n = len(nums)
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                cnt += 1
    return cnt

print("Brute Force Approach:")
print(number_of_inversions([5,4,3,2,1]))

# Optimal Approach

def merge(nums, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    cnt = 0
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            cnt += (mid - left + 1)
            right += 1

    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp[i - low]

    return cnt

def merge_Sort(nums, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += merge_Sort(nums, low, mid)
    cnt += merge_Sort(nums, mid + 1, high)
    cnt += merge(nums, low, mid, high)

    return cnt

def number_of_inversions(nums):
    return merge_Sort(nums, 0, len(nums) - 1)

print("Optimal Approach:")
print(number_of_inversions([5,4,3,2,1]))