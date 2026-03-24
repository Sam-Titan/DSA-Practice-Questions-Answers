# Approach 1 - Using Maps

def Union(nums1, nums2, n, m):
    hash_map = {}

    for i in range(n):
        hash_map[nums1[i]] = hash_map.get(nums1[i], 0) + 1
    for j in range(m):
        hash_map[nums2[j]] = hash_map.get(nums2[j], 0) + 1
    
    u = []
    for i in hash_map:
        u.append(i)

    return u

print("Approach 1 -> Using Map:")
print(Union([1,2,3,4,5], [5,6,7,8,9], 5, 5))

# Approach 2 -> Using Set

def Union(nums1, nums2):
    union = set(nums1) | set(nums2)

    return sorted(union)

print("Approach 2 -> Using Set:")
print(Union([1,2,3,4,5], [5,6,7,8,9]))

# Optimal Approach - Two pointers

def Union(nums1, nums2, n, m):
    union = []
    i = 0
    j = 0
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            if not union or nums1[i] != union[-1]:
                union.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if not union or nums2[j] != union[-1]:
                union.append(nums2[j])
            j += 1
        else:
            if not union or nums1[i] != union[-1]:
                union.append(nums1[i])
            i += 1
            j += 1
    while i < n:
        if not union or nums1[i] != union[-1]:
            union.append(nums1[i])
            i += 1
    while j < m:
        if not union or nums2[j] != union[-1]:
            union.append(nums2[j])
            j += 1
    return union

print("Optimal Approach -> Two Pointers:")
print(Union([1,2,3,4,5], [5,6,7,8,9], 5, 5))