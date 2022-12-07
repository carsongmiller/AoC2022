from timeit import default_timer as timer

lines = str()
with open('02.txt') as f:
    # lines = [int(n) for n in f.readlines()]

	lines = [line.split() for line in f.readlines()]

def part1(lines):
	score = 0

	for line in lines:
		p1 = ord(line[0]) - 64
		p2 = ord(line[1]) - 87
		score += getScore(p1, p2)
	
	return score

def part2(lines):
	score = 0

	for line in lines:
		p1 = ord(line[0]) - 64
		p2 = 0
		if line[1] == 'X':
			p2 = (p1 + 1) % 3 + 1
		elif line[1] == 'Y':
			p2 = p1		
		elif line[1] == 'Z':
			p2 = (p1 % 3) + 1

		score += getScore(p1, p2)
	
	return score

def getScore(player1, player2):
	if player1 == player2:
		return player2 + 3
	if (player2 - player1 + 3) % 3 == 1:
		return player2 + 6
	else:
		return player2


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