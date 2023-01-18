from timeit import default_timer as timer
import re
import functools

with open('16.txt') as f:
	input = f.read().strip().split('\n')

class Chamber:
	neighbors = []

	def __init__(self, name, flowrate, neighbors_str):
		self.name = name
		self.flowrate = flowrate
		self.neighbors_str = neighbors_str
		self.open = False

	def populateRealNeighbors():
		pass

	def neighborListStr(self):
		n_str = ""
		if self.neighbors != None:
			n_str = ', '.join([x.name for x in self.neighbors])
		return n_str

	def __str__(self):
		return f"{self.name}, {self.flowrate}, [{self.neighborListStr()}]"

	def __repr__(self):
		return f"{self.name} => ({self.neighborListStr()})"

class Step:
	# action 0 = open valve
	# action 1 = move to new chamber
	def __init__(self, action: int, moveto: str):
		self.action = action
		self.moveto = moveto

	def __repr__(self):
		if self.action == 0:
			return "Open Valve"
		else:
			return f"Move to {self.moveto}"

chambers_dict = {}

def part1(lines):
	pattern = r"^Valve ([A-Z]{2}) has flow rate=(\d*); tunnel[s]* lead[s]* to valve[s]* (.*)$"
	for line in lines:
		name, flowrate, neighbors = re.search(pattern, line).groups()
		neighbors = neighbors.split(', ')
		chambers_dict[name] = (Chamber(name, int(flowrate), neighbors))

	generateChamberNeighbors(chambers_dict)

	# enumerate the possible paths and valve opening combinations
	return GetMaxPressureRelief(frozenset(), 30, 'AA')

def part2(lines):
	return GetMaxPressureRelief(frozenset(), 26, 'AA', True)



# returns the pressure released by the best path starting from the given room with the given amount of time remaining
@functools.cache
def GetMaxPressureRelief(opened, mins_remaining, currentChamberName, elephant = False):
	if mins_remaining <= 0: # add current plan to plans, return
		if elephant:
			return GetMaxPressureRelief(opened, 26, 'AA')
		else:
			return 0

	currentChamber = chambers_dict[currentChamberName]

	# we're going to find the maxRelief based on if we visited each neighbor with and without opening this valve

	maxRelief = 0 #max pressure relief from this point onward

	# first, try moving to each neighbor without opening this valve
	for neighbor in currentChamber.neighbors:
		maxRelief = max(maxRelief, GetMaxPressureRelief(opened, mins_remaining - 1, neighbor.name, elephant))

	# now, try opening the valve, decreasing the time, then moving to each neighbor
	if currentChamberName not in opened and currentChamber.flowrate > 0 and mins_remaining > 1:
		opened = set(opened)
		opened.add(currentChamberName)
		mins_remaining -= 1

		# calc the total that will be released by this valve for the rest of the time
		releasedByThisValve = mins_remaining * currentChamber.flowrate

		for neighbor in currentChamber.neighbors:
			maxRelief = max(maxRelief, releasedByThisValve + GetMaxPressureRelief(frozenset(opened), mins_remaining, currentChamberName, elephant))
	
	return maxRelief


def generateChamberNeighbors(chamber_dict: dict[str, Chamber]):
	for name, chamber in chamber_dict.items():
		# add neighbors
		chamber.neighbors = []

		for neighbor_str in chamber.neighbors_str:
			for name_checking, chamber_checking in chamber_dict.items():
				if name_checking == neighbor_str:
					chamber.neighbors.append(chamber_checking)
					break

# performs deep copy of a plan (list of steps)
def CopyPlan(plan: list[Step]):
	return [Step(step.action, step.moveto) for step in plan]

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