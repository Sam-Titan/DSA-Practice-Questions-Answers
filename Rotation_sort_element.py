def rotation(nums, target):
    hash_map = [(val, idx) for idx, val in enumerate(nums)]
    hash_map.sort()
    print(hash_map)
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if hash_map[mid][0] == target:
            return hash_map[mid][1]
        elif hash_map[mid][0] < target:
            low += 1
        else:
            high -= 1

print(rotation([4,5,0,1,2], 0))
        