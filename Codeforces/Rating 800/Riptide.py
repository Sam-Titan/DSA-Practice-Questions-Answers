# A. Riptide
# time limit per test1 second
# memory limit per test256 megabytes
# Alice, Bob, and Charlie are playing a game with tokens. They start with a
# , b
# , and c
#  tokens, respectively.

# The game is played in rounds. Before the beginning of each round, they check the number of tokens everyone has:

# If any two players have the exact same number of tokens, the game immediately ends.
# Otherwise, the round begins, all three players have a strictly different number of tokens. The player with the strictly most tokens gives exactly 1
#  token to the player with the strictly fewest tokens.
# Given the starting tokens a
# , b
# , and c
# , determine exactly how many rounds the game will last before it ends.

# Input
# The first line contains a single integer t
#  (1≤t≤103
# ) — the number of test cases.

# Each test case consists of a single line containing three integers a
# , b
# , and c
#  (1≤a,b,c≤10
# ).

# Output
# For each test case, output a single integer — the number of rounds the game will last before it ends.

n = int(input())

for _ in range(n):
    max_reduction = 100
    nums = list(map(int, input().split()))
    for i in range(-1, len(nums) - 1):
        max_reduction = min(abs(nums[i] - nums[i + 1]), max_reduction)
    print(max_reduction)