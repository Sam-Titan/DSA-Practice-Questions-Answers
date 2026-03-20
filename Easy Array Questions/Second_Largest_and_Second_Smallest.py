# Brute Force

def second_smallest_and_largest(arr):
    n = len(arr)
    if n < 2:
        return -1
    
    arr.sort()
    second_largest = arr[n - 2]
    second_smallest = arr[1]
    return second_largest, second_smallest

print("Brute Force Method:")
print(second_smallest_and_largest([1,4,2,3,5]))

# Better Method

def second_smallest_and_largest(arr):
    n = len(arr)
    if n < 2:
        return -1
    
    largest = 0
    smallest = 0

    largest = max(arr)
    smallest = min(arr)

    second_largest = 0
    second_smallest = largest

    for i in range(n):
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
        if arr[i] < second_smallest and arr[i] != smallest:
            second_smallest = arr[i]
    
    return second_smallest, second_largest

print("Better Method:")
print(second_smallest_and_largest([1,4,2,3,5]))

# Optimal Method

def second_smallest(arr):
    n = len(arr)
    if n < 2:
        return -1
    
    smallest = float("inf")
    second_smallest = float("inf")

    for i in range(len(arr)):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] < second_smallest and arr[i] != smallest:
            second_smallest = arr[i]
    return second_smallest

def second_largest(arr):
    n = len(arr)
    if n < 2:
        return -1
    
    largest = float("-inf")
    second_largest = float("-inf")

    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return second_largest

print("Optimal Method:")
print(second_smallest([1,4,2,3,5]))
print(second_largest([1,4,2,3,5]))