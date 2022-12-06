import re
import numpy as np


def split_every_nth(string: str, n):
    return [string[i:i + n] for i in range(0, len(string), n)]


def findAlphabetic(string):
    result = re.findall("[A-Z]", string)
    return result[0] if len(result) == 1 else ""


def pretty_print(stacks):
    for i in range(len(stacks)):
        row = f"{i} "
        for j in range(len(stacks[i])):
            char = stacks[i][j]
            row += f" {char} "
            if j < len(stacks[i]) - 1:
                row += "-> "
        print(row)




def solvePart1(data):
    result = ""
    raw_stacks, raw_moves = data.split("\n\n")
    raw_stacks = raw_stacks.split("\n")
    stack_size = len(re.findall("\d", raw_stacks.pop()))
    print(f"Stack size is {stack_size}")
    stacks = [[] for i in range(stack_size)]
    print(f"Initial stacks {stacks}")
    for row in reversed(raw_stacks):
        crates = list(map(findAlphabetic, split_every_nth(row, 4)))
        for i, crate in enumerate(crates):
            if crate != "":
                stacks[i].append(crate)

    # print(raw_moves)
    moves = raw_moves.split("\n")

    # print(stacks)
    pretty_print(stacks)

    for move in moves:
        move = re.findall("\d+", move)
        amount = int(move[0])
        move_from = int(move[1]) - 1
        move_to = int(move[2]) - 1
        print(f"###### size {amount} from {move_from} to {move_to} ########")
        for i in range(amount):

            if len(stacks[move_from]) > 0:
                print(f"Moving {stacks[move_from][-1]}")
                stacks[move_to].append(stacks[move_from].pop())
            else:
                print(f"stacks {move_from} is empty!!!!")
            pretty_print(stacks)

    for i in range(stack_size):
        result += stacks[i][-1] if len(stacks[i]) > 0 else ""

    pretty_print(stacks)
    # print(split_every_nth(raw_stacks[1],4))
    # print(raw_moves)

    return result


def solvePart2(data):
    result = ""
    raw_stacks, raw_moves = data.split("\n\n")
    raw_stacks = raw_stacks.split("\n")
    stack_size = len(re.findall("\d", raw_stacks.pop()))
    print(f"Stack size is {stack_size}")
    stacks = [[] for i in range(stack_size)]
    print(f"Initial stacks {stacks}")
    for row in reversed(raw_stacks):
        crates = list(map(findAlphabetic, split_every_nth(row, 4)))
        for i, crate in enumerate(crates):
            if crate != "":
                stacks[i].append(crate)

    # print(raw_moves)
    moves = raw_moves.split("\n")

    # print(stacks)
    pretty_print(stacks)

    for move in moves:
        move = re.findall("\d+", move)
        amount = int(move[0])
        move_from = int(move[1]) - 1
        move_to = int(move[2]) - 1
        print(f"###### size {amount} from {move_from} to {move_to} ########")
        stacks[move_to] += stacks[move_from][-amount:]
        del stacks[move_from][-amount:]

        pretty_print(stacks)

    for i in range(stack_size):
        result += stacks[i][-1] if len(stacks[i]) > 0 else ""

    pretty_print(stacks)
    # print(split_every_nth(raw_stacks[1],4))
    # print(raw_moves)

    return result


input = open("input_day05.txt", "r")
parsed = input.read()
input.close()

arr = [1, 2 , 3 , 4]
arr2 = [5, 6, 7]
arr += arr2[-2:]
print(arr)
# part1 = solvePart1(parsed)
part2 = solvePart2(parsed)

# print(f"Part1: {part1}")  # CMZ
print(f"Part2: {part2}")

