# Brute Force Method

def is_sorted(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False
    return True

print("Brute Force Method:")
print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 2, 3, 5, 4]))


# Optimal Method

def is_sorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True


print("\nOptimal Method:")
print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 2, 3, 5, 4]))
