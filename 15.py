from timeit import default_timer as timer

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
	max = 4000000
	sbPairs = getSBPairs(lines)

	all_gaps = {}

	# build list of boundaries
	for pair in sbPairs:
		s = pair[0]
		b = pair[1]

		man = manhattan(s, b) #distance between sensor and beacon		

		pos_top = (True, s[1] + s[0] + man + 1)
		pos_bot = (True, s[1] + s[0] - man - 1)

		neg_top = (False, s[1] - s[0] + man + 1)
		neg_bot = (False, s[1] - s[0] - man - 1)

		for gap in [pos_top, pos_bot, neg_top, neg_bot]:
			if gap in all_gaps:
				all_gaps[gap] += 1
			else:
				all_gaps[gap] = 1

	gaps_pos = []
	gaps_neg = []

	for gap, count in all_gaps.items():
		if count > 1:
			if gap[0]:
				gaps_pos.append(gap[1])
			else:
				gaps_neg.append(gap[1])

	intersections = []

	for candidate_pos in gaps_pos:
		for candidate_neg in gaps_neg:
			# if candidates add up to an odd number, they won't work
			if (candidate_pos + candidate_neg) % 2 == 0:
				y = (candidate_pos + candidate_neg) // 2
				x = (candidate_pos - candidate_neg) // 2
				if 0 <= x <= max and 0 <= y <= max and outsideAllSensors(sbPairs, x, y):
					return getTuningFreq(x, y)
	


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

def outsideAllSensors(sbPairs, x, y):
	for pair in sbPairs:
		s = pair[0]
		b = pair[1]
		sensor_range = manhattan(s, b)
		distance = manhattan(s, [x, y])
		if distance <= sensor_range:
			return False
	return True

def getTuningFreq(x, y):
	return x * 4000000 + y


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