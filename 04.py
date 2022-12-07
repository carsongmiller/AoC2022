from timeit import default_timer as timer
from collections import Counter

lines = str()
with open('04.txt') as f:
	lines = f.readlines()

def part1(lines):
	count = 0
	for line in lines:
		split = line.split(',')
		aSplit = split[0].split('-')
		bSplit = split[1].split('-')
		aStart = int(aSplit[0])
		aEnd = int(aSplit[1])
		bStart = int(bSplit[0])
		bEnd = int(bSplit[1])

		if (aStart <= bStart and aEnd >= bEnd) or (bStart <= aStart and bEnd >= aEnd):
			count += 1

	return count


def part2(lines):
	count = 0
	for line in lines:
		split = line.split(',')
		aSplit = split[0].split('-')
		bSplit = split[1].split('-')
		aStart = int(aSplit[0])
		aEnd = int(aSplit[1])
		bStart = int(bSplit[0])
		bEnd = int(bSplit[1])

		if (aStart <= bStart and aEnd >= bStart) or (bStart <= aStart and bEnd >= aStart):
			count += 1

	return count


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