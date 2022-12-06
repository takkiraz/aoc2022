import numpy as np

# Lookup Table
# - | X | Y | Z
# A | 4 | 8 | 3
# B | 1 | 5 | 9
# C | 7 | 2 | 6

score1 = np.matrix([
    [4, 8, 3],
    [1, 5, 9],
    [7, 2, 6]
])

# Lookup Table
score2 = np.matrix([
    [3, 4, 8],
    [1, 5, 9],
    [2, 6, 7]
])

f = open("input_day02.txt")
input = f.readlines()
f.close()


def part1(data):
    rounds = [line.split() for line in data]
    result = sum(score1[ord(other) - ord('A'), ord(me) - ord('X')] for other, me in rounds)
    print(f"Part 1: {result}")


def part2(data):
    rounds = [line.split() for line in data]
    result = sum(score2[ord(other) - ord('A'), ord(outcome) - ord('X')] for other, outcome in rounds)
    print(f"Part 2: {result}")

part1(input)
part2(input)