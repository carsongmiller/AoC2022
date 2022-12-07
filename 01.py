from timeit import default_timer as timer

lines = str()
with open('01.txt') as f:
    # lines = [int(n) for n in f.readlines()]
	lines = f.readlines()

def part1(lines):
	totalCounts = []
	currentCount = 0
	for line in lines:
		if line == "\n":
			totalCounts.append(currentCount)
			currentCount = 0
			continue
		else:
			currentCount += int(line)

	totalCounts.sort()
	return totalCounts[-1]

def part2(lines):
	totalCounts = []
	currentCount = 0
	for line in lines:
		if line == "\n":
			totalCounts.append(currentCount)
			currentCount = 0
			continue
		else:
			currentCount += int(line)

	totalCounts.sort()
	return totalCounts[-1] + totalCounts[-2] + totalCounts[-3]


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