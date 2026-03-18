# We have to find the maximum and minimum frequencies elements in the array.
def Count_Frequencies(arr, n):
    visited = [False] * n
    max_freq = 0
    min_freq = n
    max_Ele = 0
    min_Ele = 0
    for i in range(n):
        if visited[i]:
            continue

        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        if count > max_freq:
            max_freq = count
            max_Ele = arr[i]
        if count < min_freq:
            min_freq = count
            min_Ele = arr[i]
    
    print(f"Maximum Frequency Element is {max_Ele}")
    print(f"Minimum Frequency Element is {min_Ele}")

if __name__ == "__main__":
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(arr)
    Count_Frequencies(arr, n)