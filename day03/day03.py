import numpy as np


def find_duplicates(left: str, right: str):
    duplicates = set()
    for char in left:
        if char in right:
            duplicates.add(char)

    return duplicates


def get_priority(char):
    priority = ord(char) - ord('A') + 27
    if char >= 'a':
        priority = ord(char) - ord('a') + 1
    return priority


def sum_priorities(arr):
    total_sum = 0
    for item in arr:
        total_sum += get_priority(item)
    return total_sum


def solvePart1(data):
    result = 0
    for rucksack in data:
        length = len(rucksack)
        half_size = length // 2
        duplicates = find_duplicates(rucksack[:half_size], rucksack[-(length - half_size):])
        result += sum_priorities(duplicates)

    return result


def solvePart2(data):
    result = 0
    for i in np.arange(0, len(data), 3):
        rucksack = data[i]
        badge = None
        for item in rucksack:
            if item in data[i + 1] and item in data[i + 2]:
                badge = item
        result += get_priority(badge)
    return result


input = open("input_day03.txt", "r")
parsed = input.read().split('\n')
input.close()

part1 = solvePart1(parsed)
part2 = solvePart2(parsed)

print(f"Part1: {part1}")
print(f"Part2: {part2}")
