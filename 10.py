from timeit import default_timer as timer
from collections import Counter

with open('10.txt') as f:
	input = f.read().strip().split('\n')


def part1(instructions):
	x = 1
	currentCycle = 0

	signals = []

	for instruction in instructions:
		split = instruction.split(' ')
		
		opcode = split[0]
		args = [arg.strip() for arg in split[1:]]

		cyclesToRun = getCyclesToRun(opcode)
		
		for i in range(cyclesToRun):
			currentCycle += 1

			if currentCycle in [20, 60, 100, 140, 180, 220]:
				signals.append(currentCycle * x)

			match opcode:
				case 'noop':
					pass
				case 'addx':
					if i == 1:
						x += int(args[0])
				case _:
					pass

	return sum(signals)

		


def part2(instructions):
	x = 1
	currentCycle = 0
	hPos = 0
	CRTLines = []

	for instruction in instructions:
		split = instruction.split(' ')
		
		opcode = split[0]
		args = [arg.strip() for arg in split[1:]]

		cyclesToRun = getCyclesToRun(opcode)
		
		for i in range(cyclesToRun):
			currentCycle += 1

			# add a new line
			if (currentCycle - 1) % 40 == 0:
				CRTLines.append('')

			if hPos in range(x-1, x+2):
				CRTLines[-1] += '#'
			else:
				CRTLines[-1] += '.'

			match opcode:
				case 'noop':
					pass
				case 'addx':
					if i == 1:
						x += int(args[0])
				case _:
					pass

			hPos = (hPos + 1) % 40

	return '\n' + '\n'.join(CRTLines)


def getCyclesToRun(opcode):
	if opcode == 'noop':
		return 1
	elif opcode == 'addx':
		return 2


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