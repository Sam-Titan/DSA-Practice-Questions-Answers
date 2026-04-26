# Pattern B: Frequency Counting
# Problem type: Count how many times each element appears. Use that count to answer questions.

def count(nums):
    freq = {}
    max_val = 0
    max_count = 0
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for val, key in freq.items():
        if max_count < key:
            max_count = key
            max_val = val
    return max_val, max_count

print(count([1,2,1,2,3,2]))

# Option B: Use defaultdict or Counter

from collections import defaultdict, Counter

def count(nums):
    freq = defaultdict(int)
    max_val = 0
    max_count = 0
    for num in nums:
        freq[num] += 1
    for val, key in freq.items():
        if max_count < key:
            max_count = key
            max_val = val
    return max_val, max_count

print(count([1,2,1,2,3,2]))

def count(nums):
    freq = Counter(nums)
    max_val = 0
    max_count = 0
    for val, key in freq.items():
        if max_count < key:
            max_count = key
            max_val = val
    return max_val, max_count

print(count([1,2,1,2,3,2]))