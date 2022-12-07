from timeit import default_timer as timer
from collections import Counter

lines = str()
with open('03.txt') as f:
	lines = [line.strip() for line in f.readlines()]

def part1(lines):
	sum = 0

	for line in lines:
		h1 = line[:int(len(line)/2)]
		h2 = line[int(len(line)/2):]

		sum += getItemValue(findDuplicate(h1, h2))

	return sum


def part2(lines):
	sum = 0
	for index in range(0, len(lines), 3):
		common = findBadge(lines[index], lines[index + 1], lines[index + 2])
		sum += getItemValue(common)

	return sum

def getItemValue(c):
	try:
		return ord(c) - 96 if c.islower() else ord(c) - 38
	except:
		return 0

def findDuplicate(h1, h2):
	for char in h1:
		if h2.count(char) > 0:
			return char

def findBadge(r1, r2, r3):
	set1 = set(r1)
	set2 = set(r2)
	set3 = set(r3)

	common = set1.intersection(set2).intersection(set3)
	return list(common)[0]

start = timer()
p1 = part1(lines)
end = timer()
print("Part 1:", p1)
print("Time (msec):", (end - start) * 1000)
print()

start = timer()
p2 = part2(lines)
end = timer()
print("Part 2:", p2)
print("Time (msec):", (end - start) * 1000)
print()