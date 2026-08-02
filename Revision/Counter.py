from collections import Counter
def counter():
    s = "mississippi"

    freq = Counter(s)
    num = freq.most_common(2)
    print(num)

    nums = [1,1,2,2,2,3]
    num = Counter(nums)
    print(num.most_common(2))
    
    nums = [1, 2, 2, 3, 3, 3]
    nums = Counter(nums)
    print(nums)
        
    for key, val in freq.items():
        print("Key:", key, end=" ")
        print("val:", val)

    s= "hello"
    for i in s:
        print(i)

    freq_map = {}
    for i in s:
        freq_map[i] = freq_map.get(i, 0) + 1
    print(freq_map)

    nums = Counter(s)
    print(nums)
    return Counter("anagram") == Counter("nagaram")

if "__main__" == __name__:
    num = counter()
    print(num)