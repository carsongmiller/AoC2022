from timeit import default_timer as timer
from collections import Counter

with open('09.txt') as f:
	input = f.read().strip().split('\n')


def part1(moves):
	H = Point(0,0)
	T = Point(0,0)
	tailVisited = set()
	tailVisited.add((0,0))

	for move in moves:
		dir = move[0]
		count = int(move[2:].strip())

		for step in range(count):
			if dir == 'U':
				H.y += 1
			elif dir == 'D':
				H.y -= 1
			elif dir == 'L':
				H.x -= 1
			elif dir == 'R':
				H.x += 1

			# check if tail needs to move as well
			if  abs(H.y - T.y) > 1 or abs(H.x - T.x) > 1:
				if H.y == T.y and H.x - T.x > 1: #move tail right
					T.x += 1
				elif H.y == T.y and H.x - T.x < -1: #move tail left
					T.x -= 1
				elif H.x == T.x and H.y - T.y > 1: #move tail up
					T.y += 1
				elif H.x == T.x and H.y - T.y < -1: #move tail down
					T.y -= 1

				#if we didn't need to move in a cardinal dir, we need to move diagonal
				#figure out which diagonal now

				elif H.x > T.x and H.y > T.y: # move up-right
					T.x += 1
					T.y += 1
				elif H.x > T.x and H.y < T.y: # move down-right
					T.x += 1
					T.y -= 1
				elif H.x < T.x and H.y > T.y: # move up-left
					T.x -= 1
					T.y += 1
				elif H.x < T.x and H.y < T.y: # move down-left
					T.x -= 1
					T.y -= 1

				tailVisited.add((T.x, T.y)) # try to add the tail's new position to the set

	return len(tailVisited)


def part2(moves):
	numKnots = 10
	K = []
	for knot in range(numKnots):
		K.append(Point(0,0))
	
	tailVisited = set()
	tailVisited.add((0,0))

	for move in moves:
		dir = move[0]
		count = int(move[2:].strip())

		for step in range(count):
			if dir == 'U':
				K[0].y += 1
			elif dir == 'D':
				K[0].y -= 1
			elif dir == 'L':
				K[0].x -= 1
			elif dir == 'R':
				K[0].x += 1

			# check if each knot needs to move
			for i in range(1, numKnots):
				
				if  abs(K[i-1].y - K[i].y) > 1 or abs(K[i-1].x - K[i].x) > 1:
					if K[i-1].y == K[i].y and K[i-1].x - K[i].x > 1: #move tail right
						K[i].x += 1
					elif K[i-1].y == K[i].y and K[i-1].x - K[i].x < -1: #move tail left
						K[i].x -= 1
					elif K[i-1].x == K[i].x and K[i-1].y - K[i].y > 1: #move tail up
						K[i].y += 1
					elif K[i-1].x == K[i].x and K[i-1].y - K[i].y < -1: #move tail down
						K[i].y -= 1

					#if we didn't need to move in a cardinal dir, we need to move diagonal
					#figure out which diagonal now

					elif K[i-1].x > K[i].x and K[i-1].y > K[i].y: # move up-right
						K[i].x += 1
						K[i].y += 1
					elif K[i-1].x > K[i].x and K[i-1].y < K[i].y: # move down-right
						K[i].x += 1
						K[i].y -= 1
					elif K[i-1].x < K[i].x and K[i-1].y > K[i].y: # move up-left
						K[i].x -= 1
						K[i].y += 1
					elif K[i-1].x < K[i].x and K[i-1].y < K[i].y: # move down-left
						K[i].x -= 1
						K[i].y -= 1

			tailVisited.add((K[-1].x, K[-1].y)) # try to add the tail's new position to the set

	return len(tailVisited)


class Point:
	x = 0
	y = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y



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