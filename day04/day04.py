import numpy as np


def get_sections(elf: str):
    start, end = elf.split('-')
    sections = np.arange(start=int(start), stop=int(end) + 1)
    return sections


def solvePart1(data):
    result = 0
    for row in data:
        first, second = row.split(',')
        firstSections = get_sections(first)
        secondSections = get_sections(second)
        print(first)
        print(firstSections)
        print(second)
        print(secondSections)
        if set(firstSections).issubset(set(secondSections)) or set(secondSections).issubset(set(firstSections)):
            print(f"Iintersect1d: {np.intersect1d(firstSections, secondSections)}")
            print("Is subset!!")
            result += 1

    return result


def solvePart2(data):
    result = 0
    for row in data:
        first, second = row.split(',')
        firstSections = get_sections(first)
        secondSections = get_sections(second)
        if len(np.intersect1d(firstSections, secondSections)) > 0:
            result += 1

    return result


input = open("input_day04.txt", "r")
parsed = input.read().split('\n')
input.close()

part1 = solvePart1(parsed)
part2 = solvePart2(parsed)

print(f"Part1: {part1}")
print(f"Part2: {part2}")
