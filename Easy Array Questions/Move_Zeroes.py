# Brute Force Method

def move_zeroes(nums):
    n = len(nums)
    temp = [0] * n
    index = 0

    for i in range(n):
        if nums[i] != 0:
            temp[index] = nums[i]
            index += 1
        
    for i in range(n):
        nums[i] = temp[i]
    return nums

print("Brute Force Method:")
print(move_zeroes([1,0,0,2,2,0,3,4,5,6]))

# Optimal Approach

def move_zeroes(nums):
    n = len(nums)
    j = -1

    for i in range(n):
        if nums[i] == 0:
            j = i
            break
    if j == -1:
        return
    
    for i in range(j + 1, n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1 
    return nums

print("Optimal Approach:")
print(move_zeroes([1,0,0,2,2,0,3,4,5,6]))
