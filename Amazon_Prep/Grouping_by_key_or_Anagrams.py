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