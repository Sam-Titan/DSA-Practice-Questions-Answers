# Brute Force Approach

def reverse_pairs(nums, n):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
                cnt += 1
    return cnt

print("Brute Force Approach:")
print(reverse_pairs([1,3,2,3,1], 5))

# Optimal Approach

def merge(nums, low, mid, high):
    temp = []
    left = low
    right = mid + 1        
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
    while left <= mid:
        temp.append(nums[left])
        left += 1
    while right <= high:
        temp.append(nums[right])
        right += 1
    for i in range(low, high + 1):
        nums[i] = temp[i - low]
            
def count_pairs(nums, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and nums[i] > 2 * nums[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt
        
def merge_sort(nums, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += merge_sort(nums, low, mid)
    cnt += merge_sort(nums, mid + 1, high)
    cnt += count_pairs(nums, low, mid, high)
    merge(nums, low, mid, high)
    return cnt

def count_reverse_pairs(nums):
    return merge_sort(nums, 0, len(nums) - 1)

print("Optimal Approach:")
print(count_reverse_pairs([1,3,2,3,1]))