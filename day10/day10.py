def solvePart1(data):
    result = 0
    queue = [1]
    stack = [1]
    for instruction in data:
        last = queue[-1]
        if len(stack) > 0:
            last = stack.pop()
        match instruction.split():
            case ["noop"]: queue.append(last)
            case ["addx", val]: 
                computed = last + int(val)
                stack.append(computed)
                queue += [last, last]
            
    # print(f"CyltheTH: {queue[20]}")
    # print(f"CyltheTH: {queue[60]}")
    # print(f"CyltheTH: {queue[100]}")
    # print(f"CyltheTH: {queue[140]}")
    # print(f"CyltheTH: {queue[180]}")
    # print(f"CyltheTH: {queue[220]}")
    # print(queue[180:221])
    # print(queue[0:22])
    # print(len(queue))

    result += queue[20] * 20
    result += queue[60] * 60
    result += queue[100] * 100
    result += queue[140] * 140
    result += queue[180] * 180
    result += queue[220] * 220    
    
    return queue


def solvePart2(queue):
    result = 0
    display = [[] for _ in range(6)]
    for i in range(len(queue)-1):
        height = i // 40
        width = i % 40
        sprite = [ "." for _ in range(40)]
        mid = queue[i+1]
        sprite[mid-1:mid+1] = ["#","#",'#']
        display[height].append(sprite[width])
        #print(f"Cycle: {i+1} Mid: {mid}")
        # print("Sprite: ", "".join(sprite))        

    for i in range (len(display)):
        print("".join(display[i]))
    return result


f = open("input.txt", "r")
input = f.read().splitlines()
f.close()


part1 = solvePart1(input)
part2 = solvePart2(part1)
