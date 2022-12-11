from typing import List
import re
import operator
import numpy as np

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

class Monkey:
    def __init__(self, items: List[int], divisibleBy: int, trueMonkey: int, falseMonkey: int, operationRaw: str):
        self.items = items
        self.divisibleBy = divisibleBy
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.operationRaw = operationRaw
        self.inspectedItems = 0
    
    def caclulateWorryLevel(self, old: int) -> int:
        match self.operationRaw.split("=")[1].split():
                    case ["old", op, "old"]:
                        return ops[op](old, old)
                    case ["old", op, val]:  
                        return ops[op](old, int(val))
        return int("-inf")

def printInspectedItems(monkeys: List[Monkey]):
    for i in range(len(monkeys)):
        print(f"Monkey {i}: {monkeys[i].inspectedItems}")


def solvePart1(data: List[str]):
    result = 0
    monkeys: List[Monkey] = []
    for monkeyRaw in data:
        monkeyRawArr = monkeyRaw.split("\n")
        items = [int(x) for x in monkeyRawArr[1].split(": ")[1].split(", ")]
        divisibleBy = int(re.findall("\d+",monkeyRawArr[3])[0])
        tMonkey = int(re.findall("\d+",monkeyRawArr[4])[0])
        fMonkey = int(re.findall("\d+",monkeyRawArr[5])[0])
        monkey = Monkey(items, divisibleBy, tMonkey, fMonkey, monkeyRawArr[2])
        monkeys.append(monkey)

    rounds = 20
    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.items[:]:
                worryLevel = monkey.caclulateWorryLevel(item)
                worryLevel = worryLevel // 3
                test = worryLevel % monkey.divisibleBy == 0
                if test:
                    monkeys[monkey.trueMonkey].items.append(worryLevel)
                else:
                    monkeys[monkey.falseMonkey].items.append(worryLevel)
                monkey.inspectedItems += 1
                monkey.items.remove(item)
    
    inspectedItems = [x.inspectedItems for x in monkeys]
    inspectedItems.sort(reverse=True)
    result = inspectedItems[0] * inspectedItems[1]
    print("Part1: ", result)

    return result


def solvePart2(data):
    result = 0
    monkeys: List[Monkey] = []
    for monkeyRaw in data:
        monkeyRawArr = monkeyRaw.split("\n")
        items = [int(x) for x in monkeyRawArr[1].split(": ")[1].split(", ")]
        divisibleBy = int(re.findall("\d+",monkeyRawArr[3])[0])
        tMonkey = int(re.findall("\d+",monkeyRawArr[4])[0])
        fMonkey = int(re.findall("\d+",monkeyRawArr[5])[0])
        monkey = Monkey(items, divisibleBy, tMonkey, fMonkey, monkeyRawArr[2])
        monkeys.append(monkey)

    modulo = np.lcm.reduce(list(map(lambda m: m.divisibleBy, monkeys)))
    for round in range(1, 10001):
        for monkey in monkeys:
            for item in monkey.items[:]:
                worryLevel = monkey.caclulateWorryLevel(item) % modulo
                test = worryLevel % monkey.divisibleBy == 0
                if test:
                    monkeys[monkey.trueMonkey].items.append(worryLevel)
                else:
                    monkeys[monkey.falseMonkey].items.append(worryLevel)
                monkey.inspectedItems += 1
                monkey.items.remove(item)
        # if (round == 1 or round == 20 or round == 1000 or round == 10000):
        #     print("Round ", round)
        #     printInspectedItems(monkeys)
        #     print("\n")

    inspectedItems = [x.inspectedItems for x in monkeys]
    inspectedItems.sort(reverse=True)
    result = inspectedItems[0] * inspectedItems[1]
    print("Part2: ", result)

    return result



f = open("input.txt", "r")
input = f.read().split("\n\n")
f.close()


part1 = solvePart1(input)
part2 = solvePart2(input)
