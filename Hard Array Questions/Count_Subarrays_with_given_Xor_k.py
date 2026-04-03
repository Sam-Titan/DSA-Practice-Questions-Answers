# Brute Force Approach

def countSubarraysXOR(A, B):
    count = 0
    for i in range(len(A)):
        xorVal = 0
        for j in range(i, len(A)):
            xorVal ^= A[j]
            if xorVal == B:
                count += 1
    return count

print("Brute Force Approach:")
print(countSubarraysXOR([4,2,2,6,4], 6))

# Optimal Approach

def countSubarrays(A, k):
    count = 0
    freq = {0:1}
    prefixXor = 0
    for num in A:
        prefixXor ^= num
        target = prefixXor ^ k
        if target in freq:
            count += 1
        freq[prefixXor] = freq.get(prefixXor, 0) + 1
    return count

print("Optimal Approach:")
print(countSubarraysXOR([4,2,2,6,4], 6))