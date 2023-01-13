from timeit import default_timer as timer
from collections import Counter
from functools import cmp_to_key
import numpy as np
import math

with open('15.txt') as f:
	input = f.read().strip().split('\n')

def part1(lines):
	yTarget = 2000000
	covered = set()
	beaconsAtTarget = set()
	sensorsAtTarget = set()

	sbPairs = getSBPairs(lines)

	for sbPair in sbPairs:
		s = sbPair[0]
		b = sbPair[1]

		if s[1] == yTarget:
			sensorsAtTarget.add(s[0])
		if b[1] == yTarget:
			beaconsAtTarget.add(b[0])

		# calculate manhattan distance
		man = manhattan(s, b)

		# calculate distance from sensor to target Y (2,000,000)
		yDiff = abs(s[1] - yTarget)

		# only check this beacon/sensor if its "diamond" crosses yTarget
		if man >= yDiff:
			width = 2 * abs(man - yDiff) + 1

			# add all covered points to the "covered" set
			radius = int((width - 1) / 2)
			xStart = s[0] - radius
			xStop = s[0] + radius
			for x in range(xStart, xStop + 1):
				covered.add(x)
	
	return len(covered) - len(sensorsAtTarget) - len(beaconsAtTarget)
	


def part2(lines):
	max = 20
	sbPairs = getSBPairs(lines)


def getSBPairs(lines: list[str]):
	sbPairs = []

	for line in lines:
		sensorHalf, beaconHalf = line.split(": closest beacon is at x=")
		sensorHalf = sensorHalf.split("Sensor at x=")[1]
		s = [int(x) for x in sensorHalf.split(", y=")]
		b = [int(x) for x in beaconHalf.split(", y=")]
		sbPairs.append((s, b))
	return (sbPairs)



def manhattan(a: tuple[int, int], b: tuple[int, int]) -> int:
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


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