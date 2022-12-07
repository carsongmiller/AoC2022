from timeit import default_timer as timer
from collections import Counter

lines = str()
with open('05.txt') as f:
	text = f.read()

[rawPlies, rawMoves] = text.split('\n\n')

rawPiles = rawPlies.split('\n')
numRow = len(rawPiles) - 1
numCol = int(rawPiles[-1][-2])
rawPiles = rawPiles[:numRow]
piles = []

for col in range(numCol):
	pile = ''
	for row in range(numRow):
		crate = rawPiles[(row + 1) * -1][col * 4 + 1:col * 4 + 2]
		if crate != ' ':
			pile += crate
		else:
			break
	piles.append(pile)

rawMoves = rawMoves.strip().split('\n')
moves = []
for move in rawMoves:
	moveSplit = move.split()
	moves.append([int(moveSplit[1]), int(moveSplit[3]) - 1, int(moveSplit[5]) - 1])

def part1(piles, moves):
	localPiles = []
	for pile in piles:
		localPiles.append(pile)

	localMoves = []
	for move in moves:
		localMoves.append(move)

	for move in localMoves:
		localPiles[move[2]] += localPiles[move[1]][len(localPiles[move[1]]) - move[0]:][::-1]
		localPiles[move[1]] = localPiles[move[1]][:len(localPiles[move[1]]) - move[0]]

	answer = ''
	for pile in localPiles:
		answer += pile[-1]
	return answer


def part2(piles, moves):
	localPiles = []
	for pile in piles:
		localPiles.append(pile)

	localMoves = []
	for move in moves:
		localMoves.append(move)

	for move in localMoves:
		localPiles[move[2]] += localPiles[move[1]][len(localPiles[move[1]]) - move[0]:]
		localPiles[move[1]] = localPiles[move[1]][:len(localPiles[move[1]]) - move[0]]

	answer = ''
	for pile in localPiles:
		answer += pile[-1]
	return answer


start = timer()
p1 = part1(piles, moves)
end = timer()
print("Part 1:", p1)
print("Time (msec):", (end - start) * 1000)
print()

start = timer()
p2 = part2(piles, moves)
end = timer()
print("Part 2:", p2)
print("Time (msec):", (end - start) * 1000)
print()