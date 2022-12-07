from timeit import default_timer as timer
from collections import Counter

lines = str()
with open('06.txt') as f:
	input = f.read()


def part1(text):
	for i in range(len(text) - 3):
		if len(set(text[i : i + 4])) == 4:
			print(set(text[i : i + 4]))
			return i + 4

def part2(text):
	for i in range(len(text) - 14):
		if len(set(text[i : i + 14])) == 14:
			print(set(text[i : i + 14]))
			return i + 14


start = timer()
p1 = part1(input)
end = timer()
print("Part 1:", p1)
print("Time (msec):", (end - start) * 1000)
print()

start = timer()
p2 = part2(input)
end = timer()
print("Part 2:", p2)
print("Time (msec):", (end - start) * 1000)
print()