# An elephant wants to visit his friend at point x. He lives at point 0 on the coordinate line. He can only take 1,2,3,4, and 5 steps. How many minimum steps does he need to cover the distance?

def Elephant(x):
    if x % 5 != 0:
        n = x // 5
        n += 1
    else:
        n = x // 5
    return n

print(Elephant(5))
print(Elephant(12))