from timeit import default_timer as timer
from collections import Counter

with open('11.txt') as f:
	input = f.read().strip().split('\n\n')

def part1(monkeyDescs):
	monkeys = buildMonkeys(monkeyDescs)
	rounds = 20
	mod_total = 1
	for testK in [m.testK for m in monkeys]:
		mod_total *= testK

	for round in range(rounds):
		runMonkeyRound(monkeys, mod_total)

	return calcMonkeyBusiness(monkeys)
		

def part2(monkeyDescs):
	monkeys = buildMonkeys(monkeyDescs)
	rounds = 10000
	mod_total = 1
	for testK in [m.testK for m in monkeys]:
		mod_total *= testK

	for round in range(rounds):
		runMonkeyRound(monkeys, mod_total, False)

	return calcMonkeyBusiness(monkeys)

def printInspections(monkeys):
	for monkey in monkeys:
		print("Monkey ", monkey.number, ": ", monkey.inspections)

def calcMonkeyBusiness(monkeys):
	first = 0
	second = 0
	for monkey in monkeys:
		if monkey.inspections > first:
			second = first
			first = monkey.inspections
		elif monkey.inspections > second:
			second = monkey.inspections

	return first * second

def buildMonkeys(descriptions):
	monkeys = []
	for desc in descriptions:
		monkeys.append(Monkey(desc))

	return monkeys

def runMonkeyRound(monkeys, mod, part1Rules = True):
	for monkey in monkeys:
		for item in monkey.items:
			item = inspectItem(item, monkey)
			monkey.inspections += 1

			if part1Rules:
				item = int(item / 3)

			if testItem(item, monkey.testK):
				recipient = monkeys[monkey.ifTrue]
			else:
				recipient = monkeys[monkey.ifFalse]

			if part1Rules:
				recipient.items.append(item)
			else:
				recipient.items.append(item % mod)

		monkey.items = [] # the monkey always throws all of its items

	

def inspectItem(item, monkey):

	scaleConstant = monkey.opK
	if scaleConstant == 'old':
		scaleConstant = item

	match monkey.opOp:
		case '*':
			item *= scaleConstant
		case '/':
			item /= scaleConstant
		case '+':
			item += scaleConstant
		case '-':
			item -= scaleConstant
		case _:
			print("Invalid operator: ", monkey.opOp)
	return item


def testItem(item, testConstant):
	if item % testConstant == 0:
		return True
	else:
		return False


class Monkey:
	number = -1
	items = []
	opOp = ''
	opK = None
	testK = 0
	ifTrue = 0
	ifFalse = 0
	inspections = 0

	def __init__(self, desc):
		desc = desc.strip().split('\n')
		self.number = int(desc[0].split(' ')[1][:-1])
		self.items = [int(x.strip().strip(',')) for x in desc[1].split(': ')[1].split(' ')]
		[self.opOp, self.opK] = desc[2].split('old ')[1].split(' ')
		self.opK = self.opK if self.opK == 'old' else int(self.opK)
		self.testK = int(desc[3].split('by ')[1])
		self.ifTrue = int(desc[4].split('monkey ')[1])
		self.ifFalse = int(desc[5].split('monkey ')[1])

	def __str__(self):
		s = ""
		s += "Monkey " + str(self.number) + '\n'
		s += "  Items:\t"
		for item in self.items:
			s += str(item) + ", "

		s = s.strip(', ') + '\n'
		s += '  Operation:\tnew = old ' + self.opOp + ' ' + str(self.opK) + '\n'
		s += '  Test:\t\tdivisible by ' + str(self.testK) + '\n'
		s += '    If true:\tthrow to monkey ' + str(self.ifTrue) + '\n'
		s += '    If false:\tthrow to monkey ' + str(self.ifFalse) + '\n'
		return s

	def __repr__(self):
		return str(self)

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