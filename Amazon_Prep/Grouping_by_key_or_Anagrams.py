# Pattern C: Grouping by Key
# Problem type: Group elements that share a property (anagrams share the same sorted characters).

def group(anagrams):
    general = {}
    for an in anagrams:
        new = tuple(sorted(an))
        if new not in general:
            general[new] = []
        general[new].append(an)
    return list(general.values())

print(group(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Or

from collections import defaultdict

def group(anagrams):
    general = defaultdict(list)
    for an in anagrams:
        new = tuple(sorted(an))
        general[new].append(an)
    return list(general.values())

print(group(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Given two strings s and t, return True if t is an anagram of s.

# Example:
# Input:  s = "anagram", t = "nagaram"
# Output: True

# Input:  s = "rat", t = "car"
# Output: False

def group(s, t):
    new_s = tuple(sorted(s))
    new_t = tuple(sorted(t))

    if new_s == new_t:
        return True
    else:
        return False

print(group("anagram", "nagaram"))

def group(s, t):
    if len(s) != len(t):
        return False
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in t:
        if c not in freq or freq[c] == 0:
            return False
        freq[c] -= 1
    return True

print(group("anagram", "nagaram"))

from collections import Counter

def group(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

print(group("anagram", "nagaram"))