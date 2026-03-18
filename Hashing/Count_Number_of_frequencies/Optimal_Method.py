# Here we will use Hashing to store the elements frequencies.

from collections import defaultdict

# Using Default Dictionary to store frequencies of elements in the array.
def Frequencies(arr, n):
    freq_map = defaultdict(int)
    for i in range(n):
        freq_map[arr[i]] += 1
    for key, value in freq_map.items():
        print(f"{key}, {value}")

if __name__ == "__main__":
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(arr)
    Frequencies(arr, n)

# Usiing Array Hashing to store frequencies of elements in the array.
def Frequencies(arr, n):
    arr_map = [0] * (max(arr) + 1)
    for i in range(n):
        arr_map[arr[i]] += 1
    for i in range(len(arr_map)):
        if arr_map[i] > 0:
            print(f"{i}, {arr_map[i]}")

if __name__ == "__main__":
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(arr)
    Frequencies(arr, n)

# Using manually made dictionary to store frequencies of elements in the array.
def Frequencies(arr, n):
    freq_map = {}

    for i in range(n):
        freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
    for key, value in freq_map.items():
        print(f"{key}, {value}")

if __name__ == "__main__":
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(arr)
    Frequencies(arr, n)