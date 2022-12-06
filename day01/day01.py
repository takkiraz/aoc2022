
input = open("input_day01.txt", "r")

parsed = input.read().split("\n\n")

input.close()

splitLinebreak = lambda x: sum([int(val) for val in x.split("\n")])
parsed = list(map(splitLinebreak, parsed))

print(type(parsed))
parsed.sort(reverse=True)
print(parsed)
top3 = parsed[:3]
print(top3)
print("Sum of Top 3: ", sum(top3))