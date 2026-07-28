def palindrom(i, s):
    if i >= len(s) // 2:
        return True

    if s[i] != s[len(s) - i - 1]:
        return False

    return palindrom(i + 1, s)

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(palindrom(0, s))