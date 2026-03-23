def linear_search(nums, num, n):
    for i in range(n):
        if nums[i] == num:
            return i
        
    return -1

print("Print the index of the number if found or else -1 if not found:", linear_search([1,2,3,4,5], 3, 5))
