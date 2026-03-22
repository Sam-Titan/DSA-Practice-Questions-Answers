# Brute Force Method

def removeDuplicates(arr):
    seen = set()

    index = 0
    for num in arr:
        if num not in seen:
            seen.add(num)
            arr[index] = num
            index += 1
    return index 

print("Solved using Set:")
print(removeDuplicates([1,1,2,3,4,5]))

# Optimal Method

def removeDuplicates(arr):
    if not arr:
        return 0
    
    i = 0 
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

print("Solved using Two pointer Approach:")
print(removeDuplicates([1,1,2,3,4,5]))