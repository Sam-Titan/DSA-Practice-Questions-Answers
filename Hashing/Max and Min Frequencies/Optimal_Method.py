# Here we will use Hashing to store the elements frequencies and find the max and min frequency element.

from collections import defaultdict

# Using Default Dictionary to store frequencies of elements in the array and find the max and min frequency element.
def Frequencies(arr, n):
    max_freq = 0
    min_freq = n
    max_Ele = 0
    min_Ele = 0
    freq_map = defaultdict(int)
    for i in range(n):
        freq_map[arr[i]] += 1
    for key, value in freq_map.items():
        if value > max_freq:
            max_freq = value
            max_Ele = key
        if value < min_freq:
            min_freq = value
            min_Ele = key
    print(f"Maximum Frequency Element is {max_Ele}")
    print(f"Minimum Frequency Element is {min_Ele}")

if __name__ == "__main__":
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(arr)
    Frequencies(arr, n)

# Usiing Array Hashing to store frequencies of elements in the array and find the max and min frequency element.
def Frequencies(arr, n):
    max_Ele = 0
    min_Ele = 0
    arr_map = [0] * (max(arr) + 1)
    for i in range(n):
        arr_map[arr[i]] += 1
    max_Ele = arr_map.index(max(arr_map))
    min_Ele = arr_map.index(min([i for i in arr_map if i > 0]))
    print(f"Maximum Frequency Element is {max_Ele}")
    print(f"Minimum Frequency Element is {min_Ele}")

if __name__ == "__main__":
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(arr)
    Frequencies(arr, n)

# Using manually made dictionary to store frequencies of elements in the array and find the max and min frequency element.
def Frequencies(arr, n):
    freq_map = {}
    max_freq = 0
    min_freq = n
    max_Ele = 0
    min_Ele = 0

    for i in range(n):
        freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
    for key, value in freq_map.items():
        if value > max_freq:
            max_freq = value
            max_Ele = key
        if value < min_freq:
            min_freq = value
            min_Ele = key
    print(f"Maximum Frequency Element is {max_Ele}")
    print(f"Minimum Frequency Element is {min_Ele}")

if __name__ == "__main__":
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(arr)
    Frequencies(arr, n)