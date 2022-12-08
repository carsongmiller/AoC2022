from timeit import default_timer as timer
from collections import Counter

with open('08.txt') as f:
	input = f.read().strip().split('\n')


def part1(text):

	width = len(text[0])
	height = len(text)
	treesOnEdge = width + width + height + height - 4

	# go down each row/column from each of the 4 directions.
	# along the way, add a tree to the set if it's visible from that direction

	visible = set()
	for row in range(1, height - 1):
		tallestFromLeft = int(text[row][0])
		tallestFromRight = int(text[row][-1])
		for col in range(1, width - 1):
			#go left to right
			if int(text[row][col]) > tallestFromLeft:
				visible.add((row, col))
				tallestFromLeft = int(text[row][col])

			#go right to left
			if int(text[row][width - col - 1]) > tallestFromRight:
				visible.add((row, width - col - 1))
				tallestFromRight = int(text[row][width - col - 1])

	for col in range(1, width - 1):
		tallestFromTop = int(text[0][col])
		tallestFromBottom = int(text[-1][col])
		for row in range(1, height - 1):
			#go top to bottom
			if int(text[row][col]) > tallestFromTop:
				visible.add((row, col))
				tallestFromTop = int(text[row][col])

			#go bottom to top
			if int(text[height - row - 1][col]) > tallestFromBottom:
				visible.add((height - row - 1, col))
				tallestFromBottom = int(text[height - row - 1][col])

	return len(visible) + treesOnEdge
	
	


def part2(text):
	width = len(text[0])
	height = len(text)
	bestScore = 0
	for row in range(1, height - 1):
		for col in range(1, width - 1):
			thisScore = getScore(text, row, col)
			if thisScore > bestScore:
				bestScore = thisScore

	return bestScore

def getScore(forest, row, col):
	currentHeight = int(forest[row][col])
	width = len(forest[0])
	height = len(forest)

	score_left = 0
	score_right = 0
	score_top = 0
	score_bottom = 0

	for x in range(col):
		score_left += 1
		if int(forest[row][col - x - 1]) >= currentHeight:
			break
	
	for x in range(col + 1, width):
		score_right += 1
		if int(forest[row][x]) >= currentHeight:
			break

	for y in range(row):
		score_top += 1
		if int(forest[row - y - 1][col]) >= currentHeight:
			break

	for y in range(row + 1, height):
		score_bottom += 1
		if int(forest[y][col]) >= currentHeight:
			break

	return score_left * score_right * score_top * score_bottom

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