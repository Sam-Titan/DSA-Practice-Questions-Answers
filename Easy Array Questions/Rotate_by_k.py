# Brute Force Approach

def rotate_right(nums, k):
    n = len(nums)
    k = k % n
    temp = nums[-k:]

    for i in range(n - k - 1, -1, -1):
        nums[i + k] = nums[i]
    for i in range(k):
        nums[i] = temp[i]
    return nums

def rotate_left(nums, k):
    n = len(nums)
    k = k % n
    temp = nums[:k]

    for i in range(k, n):
        nums[i - k] = nums[i]
    for i in range(k):
        nums[n - k + i] = temp[i]
    return nums

print("Brute Force Method:")
print("Rotate right:")
print(rotate_right([1,2,3,4,5], 3))
print("Rotate left:")
print(rotate_left([1,2,3,4,5], 3))

# Optimal Method
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate(nums, k, direction):
    n = len(nums)

    k = k % n

    if direction == "right":
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

    elif direction == "left":
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
        reverse(nums, 0, n - 1)

    return nums

print("Optimal Approach:")
print("Rotate right:")
print(rotate([1,2,3,4,5], 3, "right"))
print("Rotate left:")
print(rotate([1,2,3,4,5], 3, "left"))