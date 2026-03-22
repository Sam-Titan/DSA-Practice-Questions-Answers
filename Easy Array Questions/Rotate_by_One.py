# Brute Force Method

def rotate(nums):
    n = len(nums)
    temp = [0] * n

    for i in range(1, n):
        temp[i - 1] = nums[i]
    temp[-1] = nums[0]

    for i in range(n):
        nums[i] = temp[i]
    return nums

print("Brute Force Method:")
print(rotate([1,2,3,4,5]))

# Optimal Method

def rotate(nums):
    n = len(nums)
    temp = nums[0]

    for i in range(1, n):
        nums[i - 1] = nums[i]
    nums[-1] = temp

    return nums

print("Optimal Method:")
print(rotate([1,2,3,4,5]))
