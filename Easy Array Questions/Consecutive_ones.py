# Approach

def findMaxConsecutiveOnes(nums):
    total = 0
    max_total = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            total += 1
        else:
            total = 0

        if total > max_total:
            max_total = total

    return max_total

print("Approach:")
print(findMaxConsecutiveOnes([1,1,0,1,1,0,1,1,1]))
