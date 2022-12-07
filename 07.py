from timeit import default_timer as timer
from collections import Counter

lines = str()
with open('07.txt') as f:
	input = f.read()


def part1(text):
	root = discoverFiles(text)
	populateDirSizes(root)
	return countDirSizes(root, 100000)


def part2(text):
	root = discoverFiles(text)
	populateDirSizes(root)

	totalDiskSpace = 70000000
	neededSpace = 30000000

	needToFree = neededSpace - (totalDiskSpace - root.totalSize)
	return findMinimumDir(root, needToFree, root.totalSize)


# returns the size of the smallest dir that is at least "minimumSize" in total size
def findMinimumDir(root, minimumSize, currentBest):
	if root.totalSize >= minimumSize and root.totalSize < currentBest:
		currentBest = root.totalSize
	
	if root.children != None:
		for child in root.children:
			childBest = findMinimumDir(child, minimumSize, currentBest)
			if childBest >= minimumSize and childBest < currentBest:
				currentBest = childBest
	
	return currentBest

# for root and all directories within it which have a total size <= maximum, 
# returns the sum total of those sizes
def countDirSizes(root, maximum):
	totalSize = 0
	if root.totalSize <= maximum:
		totalSize += root.totalSize
	
	if root.children != None:
		for child in root.children:
			totalSize += countDirSizes(child, maximum)
	
	return totalSize

def populateDirSizes(root):
	root.totalSize = root.immediateSize
	
	if root.children != None:
		for child in root.children:
			populateDirSizes(child)
			root.totalSize += child.totalSize


def discoverFiles(text):
	lines = text.split('\n')
	currentDir = Dir()
	currentDir.name = '/'
	dirRoot = currentDir

	for line in lines[1:]:
		if len(line) == 0:
			continue

		if line[:4] == '$ cd':
			newDirName = line.strip()[5:]
			if newDirName == '..':
				currentDir = currentDir.parent
			else:
				for child in currentDir.children:
					if child.name == newDirName:
						currentDir = child
						break

		elif line[:4] == '$ ls':
			continue #don't need to do anything if it's an ls
	
		elif line[:3] == 'dir':
			newDir = Dir()
			newDir.name = line.strip()[4:]

			try:
				if currentDir.children == None:
					currentDir.children = []
				currentDir.children.append(newDir)
			except:
				pass

			try:
				newDir.parent = currentDir
			except:
				pass

		elif line[0].isnumeric():
			currentDir.immediateSize += int(line.strip().split()[0])

	return dirRoot

class Dir:
	name = ''
	immediateSize = 0
	totalSize = 0
	children = None
	parent = None


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