# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 

# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
# Example 2:

# Input: nums = [2,4,3,5,1]
# Output: 3
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -231 <= nums[i] <= 231 - 1


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