# Problem 2 — Longest Substring Without Repeating Characters ⭐⭐ (Medium)
# LeetCode 3

# Given a string s, find the length of the longest substring without repeating characters.

# Example:
# Input:  s = "abcabcbb"
# Output: 3   ← "abc"

# Input:  s = "bbbbb"
# Output: 1   ← "b"

def lengthofsubstring(s):
    left = 0
    best = 0
    seen ={}
    for right in range(len(s)):
        char = s[right]
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        best = max(best, right - left + 1)
    return best

print(lengthofsubstring("abcabcbb"))