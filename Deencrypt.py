# % print the following digit following number of times
# # leave it empty
# $ reverse the string inside

# Secret Key: mnbvcxzlkjhgfdsapoiuytrewq
# Encrypted Key: qc%3avfv#ds$wq$rv

s = input()
n = input()
t = len(n)
digit = 0
string = ""
while t > 0:
    if n[digit] == "%":
        string += f"{int(n[digit + 1]) * n[digit+2]}"
        digit += 3
        t -= 3
    elif n[digit] == "#":
        digit += 1
        t -= 1
        pass
    elif n[digit] == "$":
        temp = ""
        while True:
            digit += 1
            t -= 1
            if n[digit] == "$":
                if len(temp) >= 1:
                    for i in range(len(temp) - 1, -1, -1 ):
                        string += f"{temp[i]}"
                digit += 1
                t -= 1
                break
            k = ord(n[digit]) - 96
            temp += s[k]
    else:
        t -= 1
        k = ord(n[digit]) - 96
        string += s[k]
        digit += 1
print(string)