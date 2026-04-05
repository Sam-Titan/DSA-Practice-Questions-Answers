# Brute Force Approach

def merge(intervals):
    intervals.sort()
    n = len(intervals)
    ans = []
    i = 0
    while i < n:
        start = intervals[i][0]
        end = intervals[i][1]
        j = i + 1
        while j < n and intervals[j][0] <= end:
            end = max(intervals[j][1], end)
            j += 1
        ans.append([start, end])
        i = j
    return ans

print("Brute Force Approach:")
print(merge([[1,3],[2,6],[8,10],[15,18]]))

# Optimal Approach

def merge(intervals):
    intervals.sort()
    n = len(intervals)
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

print("Optimal Approach:")
print(merge([[1,3],[2,6],[8,10],[15,18]]))