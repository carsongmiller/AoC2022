from timeit import default_timer as timer

lines = str()
with open('1_input.txt') as f:
    lines = [int(n) for n in f.readlines()]

def part1(lines):
	count = 0
	for i in range(1, len(lines)):
		if int(lines[i]) > int(lines[i-1]):
			count += 1
	return count

def part2(lines):
	count = 0
	for i in range(3, len(lines)):
		if (int(lines[i]) > int(lines[i-3])):
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