def Count_Frequescies(arr, n):
    visited = [False] * n

    for i in range(n):
        if visited[i]:
            continue

        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        print(f"{arr[i]}, {count}")

if __name__ == "__main__":
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(arr)
    Count_Frequescies(arr, n)