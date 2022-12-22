from timeit import default_timer as timer
from collections import Counter
import math

with open('12.txt') as f:
	input = f.read().strip().split('\n')

def part1(grid):
	distances = []
	goal = None
	source = None

	for r in range(len(grid)):
		newDistanceLine = []
		for c in range(len(grid[r])):
			newDistanceLine.append(math.inf)
			if grid[r][c] == 'S':
				source = (r, c)
				grid[r] = grid[r][:c] + 'a' + grid[r][c+1:]

			if grid[r][c] == 'E':
				goal = (r, c)

		distances.append(newDistanceLine)

	dijkstra(grid, distances, source)

	return distances[goal[0]][goal[1]]	


def part2(grid):
	distances = []
	goal = None
	source = None

	for r in range(len(grid)):
		newDistanceLine = []
		for c in range(len(grid[r])):
			if grid[r][c] == 'S':
				grid[r] = grid[r][:c] + 'a' + grid[r][c+1:]
			else:
				newDistanceLine.append(math.inf)

			if grid[r][c] == 'E':
				goal = (r, c)

		distances.append(newDistanceLine)

	bestScore = math.inf
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == 'a':
				for row in distances:
					for cell in row:
						cell = math.inf
				dijkstra(grid, distances, (r, c))
				score = distances[goal[0]][goal[1]]
				bestScore = score if score < bestScore else bestScore

	return bestScore



def dijkstra(grid, distances, source):
	neighbors = [source]
	visited = []

	distances[source[0]][source[1]] = 0

	while len(neighbors) > 0:
		# select the next node we'll explore
		(r, c) = neighbors[0]
		bestD = distances[r][c]

		for neighbor in neighbors:
			if distances[neighbor[0]][neighbor[1]] < bestD:
				(r, c) = neighbor
				bestD = distances[neighbor[0]][neighbor[1]]

		neighbors.remove((r, c))
		visited.append((r, c))
		
		current = ord(grid[r][c]) - 97 if grid[r][c] != 'E' else 25

		if r - 1 >= 0:
			test = ord(grid[r - 1][c]) - 97 if grid[r - 1][c] != 'E' else 25
			if test - current <= 1 and not (r-1, c) in visited: # top is a valid neighbor
				if not (r - 1, c) in neighbors:
					neighbors.append((r - 1, c))
				if distances[r][c] + 1 < distances[r - 1][c]:
					distances[r - 1][c] = distances[r][c] + 1

		if r + 1 < len(grid):
			test = ord(grid[r + 1][c]) - 97 if grid[r + 1][c] != 'E' else 25
			if test - current <= 1 and not (r+1, c) in visited: # bottom is a valid neighbor
				if not (r + 1, c) in neighbors:
					neighbors.append((r + 1, c))
				if distances[r][c] + 1 < distances[r + 1][c]:
					distances[r + 1][c] = distances[r][c] + 1

		if c - 1 >= 0:
			test = ord(grid[r][c - 1]) - 97 if grid[r][c - 1] != 'E' else 25
			if test - current <= 1 and not (r, c - 1) in visited: # left is a valid neighbor
				if not (r, c - 1) in neighbors:
					neighbors.append((r, c - 1))
				if distances[r][c] + 1 < distances[r][c - 1]:
					distances[r][c - 1] = distances[r][c] + 1

		if c + 1 < len(grid[0]):
			test = ord(grid[r][c + 1]) - 97 if grid[r][c + 1] != 'E' else 25
			if test - current <= 1 and not (r, c + 1) in visited: # bottom is a valid neighbor
				if not (r, c + 1) in neighbors:
					neighbors.append((r, c + 1))
				if distances[r][c] + 1 < distances[r][c + 1]:
					distances[r][c + 1] = distances[r][c] + 1


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