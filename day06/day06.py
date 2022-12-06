def index_of_n_distinct_characters(string, n):
    size = len(string)
    i = 0
    while i < size - 1 - n:
        marker = set(string[i:i+n])
        if len(marker) == n:
            return i+n
        i += 1


def solvePart1(data):
    return index_of_n_distinct_characters(data, 4)


def solvePart2(data):
    return index_of_n_distinct_characters(data, 14)


f = open("input_day06.txt", "r")
parsed = f.read()
f.close()


part1 = solvePart1(parsed)
part2 = solvePart2(parsed)

print(f"Part1: {part1}")
print(f"Part2: {part2}")

