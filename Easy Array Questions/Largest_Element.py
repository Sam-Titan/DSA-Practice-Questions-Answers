# Brute Force

def Max(arr):
    arr.sort()

    return arr[len(arr) - 1]
print("Brute Force Method:")
print(Max([1,4,2,5]))

# Optimal Method

def Max(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
print("Optimal Method")
print(Max([1,4,2,5]))