from timeit import default_timer as timer
from collections import Counter
from functools import cmp_to_key
import numpy as np
import math

with open('14.txt') as f:
	input = f.read().strip().split('\n')

# 0 = air
# 1 = rock
# 2 = starting point
# 3 = falling sand
# 4 = settled sand

def part1(pairs):
	grid = buildGrid(pairs)
	startX = None
	for i in range(len(grid[0])):
		if grid[0][i] == 2:
			startX = i

	gridCopy = None

	sandDropped = 0

	while grid != gridCopy:
		gridCopy = copyGrid(grid)

		# place new sand
		grid[0][startX] = 3
		sandDropped += 1
		dropSand_part1(grid, startX, 0)

	return sandDropped - 1

def part2(pairs):
	grid = buildGrid(pairs)
	newRow = [0] * len(grid[0])
	grid.append(newRow)
	newRow = [1] * len(grid[0])
	grid.append(newRow)
	
	startX = None
	for i in range(len(grid[0])):
		if grid[0][i] == 2:
			startX = i

	gridCopy = None

	sandDropped = 0

	while grid[0][startX] != 4:
		# place new sand
		grid[0][startX] = 3
		sandDropped += 1
		dropSand_part2(grid, startX, 0)

	return sandDropped - 1

# Give a grid with a single piece of falling sand at x, y
# Modofies grid until that piece of sand is settled
def dropSand_part1(grid, x, y):
	# x,y = current position of falling sand

	while True:

		# if the sand is at the bottom, let it fall off the grid and return
		if y == len(grid) - 1:
			grid[y][x] = 0
			return

		# try to move sand directly down
		elif grid[y+1][x] == 0:
			grid[y][x] = 0
			grid[y+1][x] = 3
			y += 1

		# if we're on the left edge, we're gonna leave the grid
		elif x == 0:
			grid[y][x] = 0
			return

		# try to move sand down left
		elif grid[y+1][x-1] == 0:
			grid[y][x] = 0
			grid[y+1][x-1] = 3
			y += 1
			x -= 1

		# if we're on the right edge, we're gonna leave the grid
		elif x == len(grid[0]) - 1:
			grid[y][x] = 0
			return

		# try to move sand down right
		elif grid[y+1][x+1] == 0:
			grid[y][x] = 0
			grid[y+1][x+1] = 3
			y += 1
			x += 1

		# if none of the above works, the sand is settled
		else:
			grid[y][x] = 4
			return

# Give a grid with a single piece of falling sand at x, y
# Modofies grid until that piece of sand is settled
def dropSand_part2(grid, x, y):
	# x,y = current position of falling sand

	while True:

		# if sand is on the bottom rock floor, sand is settled
		if y == len(grid) - 2:
			grid[y][x] = 4
			return

		# try to move sand directly down
		if grid[y+1][x] == 0:
			grid[y][x] = 0
			grid[y+1][x] = 3
			y += 1

		# try to move sand down left
		elif grid[y+1][x-1] == 0:
			grid[y][x] = 0
			grid[y+1][x-1] = 3
			y += 1
			x -= 1

		# try to move sand down right
		elif grid[y+1][x+1] == 0:
			grid[y][x] = 0
			grid[y+1][x+1] = 3
			y += 1
			x += 1

		# if none of the above works, the sand is settled
		else:
			grid[y][x] = 4
			return
		

def copyGrid(grid):
	copy = []
	for row in grid:
		copy.append([])
		for col in row:
			copy[-1].append(col)

	return copy


def getGridBounds(paths):
	xLow = 1000
	xHigh = 0
	yLow = 1000
	yHigh = 0

	for path in paths:
		segments = path.split(' -> ')
		for i in range(len(segments) - 1):
			start = [int(x) for x in segments[i].split(',')]
			end = [int(x) for x in segments[i+1].split(',')]

			# check x's
			if start[0] < xLow:
				xLow = start[0]
			if end[0] < xLow:
				xLow = end[0]
			if start[0] > xHigh:
				xHigh = start[0]
			if end[0] > xHigh:
				xHigh = end[0]
			
			# check y's
			if start[1] < yLow:
				yLow = start[1]
			if end[1] < yLow:
				yLow = end[1]
			if start[1] > yHigh:
				yHigh = start[1]
			if end[1] > yHigh:
				yHigh = end[1]

	return xLow, xHigh, yLow, yHigh

def buildGrid(paths):

	xLow, xHigh, yLow, yHigh = getGridBounds(paths)
	# don't actually use yLow because it will always be >= 0, but we'll use 0 anyways

	# make the grid the appropriate size from the get to to make our life easier
	# grid = [[0] * (xHigh - xLow + 1)] * (yHigh + 1)
	grid = []
	for y in range(yHigh + 1):
		grid.append([])
		for x in range(xHigh - xLow + 1):
			grid[-1].append(0)

	grid[0][500 - xLow] = 2 # mark the starting point
	
	for path in paths:
		segments = path.split(' -> ')
		for i in range(len(segments) - 1):
			start = np.array([int(x) for x in segments[i].split(',')])
			end = np.array([int(x) for x in segments[i + 1].split(',')])

			# get unit vector in direction from start to end
			
			dist = int(np.linalg.norm(start - end))
			# norm = int(math.sqrt(dist[0] ** 2 + dist[1] ** 2))
			vector = end - start
			unit = vector / dist

			for step in range(dist + 1):
				pos = start + unit * step # get position at this step
				grid[int(pos[1])][int(pos[0]) - xLow] = 1

	return grid


def printGrid(grid):
	print('=' * len(grid[0]))
	for row in grid:
		s = ''
		for col in row:
			match col:
				case 0:
					s += '.'
				case 1: 
					s += '#'
				case 2:
					s += '+'
				case 3:
					s += 'o'
				case 4:
					s += 'X'
		print(s)
	print('=' * len(grid[0]))

			




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