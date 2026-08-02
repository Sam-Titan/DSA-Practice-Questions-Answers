def sorting():
    # Sort list of lists by second element, descending
    items = [[1, 3], [2, 1], [3, 2]]
    # items.sort(key=lambda x: x[1], reverse=True)
    # [[1,3],[3,2],[2,1]]

    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j][1] > items[min_index][1]:
                min_index = j
        items[i][1], items[i][0], items[min_index][1], items[min_index][0] = items[min_index][1], items[min_index][0], items[i][1], items[i][0]
    print(items)

    # Sort by absolute value
    nums = [-3, 1, -2, 4]
    nums.sort()
    print(nums)

    nums = sorted(nums, key=abs)      # [1,-2,-3,4]

    print(nums)

    # Sort by multiple keys: first ascending, second descending
    data = [("Alice", 3), ("Bob", 1), ("Alice", 1)]
    data.sort(key=lambda x: (x[0], -x[1]))
    # [('Alice',3),('Alice',1),('Bob',1)]
    print(data)

if "__main__" == __name__:
    sorting()