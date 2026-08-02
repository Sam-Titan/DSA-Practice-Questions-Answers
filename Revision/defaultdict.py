from collections import defaultdict

def default():
    freq_map = defaultdict(int)
    freq_map["new"] += 1

    print(freq_map)

    group = defaultdict(list)

    for word in ["eat", "ate", "tea", "tan"]:
        key = tuple(sorted(word))
        group[key].append(word)

    print(group)

if "__main__" == __name__:
    default()