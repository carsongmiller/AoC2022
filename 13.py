from timeit import default_timer as timer
from collections import Counter
from functools import cmp_to_key

with open('13.txt') as f:
	input = f.read().strip().split('\n\n')

def part1(pairs):
	indicesSum = 0
	for index in range(len(pairs)):
		[left, right] = pairs[index].strip().split('\n')

		if compareValues(left, right) == -1:
			indicesSum += index + 1

	return indicesSum


def part2(pairs):
	lines = []
	for index in range(len(pairs)):
		[left, right] = pairs[index].strip().split('\n')
		lines.append(left)
		lines.append(right)

	lines.append('[[2]]')
	lines.append('[[6]]')

	lines.sort(key = cmp_to_key(compareValues))
	return (lines.index('[[2]]') + 1) * (lines.index('[[6]]') + 1)
	
def compareValues(left, right):
	leftBracketed = bracketed(left)
	rightBracketed = bracketed(right)

	# if both are numeric, compare and return 
	if left.isnumeric() and right.isnumeric():
		if int(left) < int(right):
			return -1
		elif int(left) > int(right):
			return 1
		else:
			return 0

	# if both are surrounded by brackets, get list of elements then test each pair
	elif leftBracketed and rightBracketed:
		items_l = getListItems(left)
		items_r = getListItems(right)

		# compare all items until we find an answer or one (or both) runs out of items
		while len(items_l) > 0 and len(items_r) > 0:
			result = compareValues(items_l[0], items_r[0])
			if result != 0:
				return result

			items_l = items_l[1:]
			items_r = items_r[1:]

		# if we've run out of items in one list, return accordingly
		if len(items_l) == 0 and len(items_r) > 0:
			return -1
		elif len(items_l) > 0 and len(items_r) == 0:
			return 1
		else:
			return 0

	# if mixed types, add brackets and then call recursively
	elif leftBracketed and not rightBracketed:
		return compareValues(left, '[' + right + ']')

	elif rightBracketed and not leftBracketed:
		return compareValues('[' + left + ']', right)


def getListItems(expr):
	items = []
	parenCount = 0
	i = 0
	expr = expr[1:-1]

	while i < len(expr):
		if expr[i] == '[':
			parenCount += 1
		elif expr[i] == ']':
			parenCount -= 1
		elif expr[i] == ',' and parenCount == 0:
			items.append(expr[:i])
			expr = expr[i:].strip(',')
			i = 0
			continue
		i += 1

	if len(expr) > 0:
		items.append(expr)
	return items

def bracketed(expr):
	parenCount = 0

	# catch quick basic cases
	if len(expr) == 0 or expr[0] != '[' or expr[-1] != ']':
		return False

	for i in range(len(expr)):
		if expr[i] == '[':
			parenCount += 1
		elif expr[i] == ']':
			parenCount -= 1
		
		# if we've fully closed a pair of parens and we're not at the end, we're not bracketed
		if parenCount == 0 and i < len(expr) - 1:
			return False

	# if we haven't returned by now, we're bracketed
	return True

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