import re


PATTERN = r":(.*)\|(.*)"


def strToSet(input):
	return frozenset(map(int, filter(None, input.strip().split(' '))))

def numWinning(card):
	return len(set(card[0]).intersection(set(card[1])))

def parseInput(path):
	with open(path, 'r') as file:
		cards = filter(None, [next(iter(re.findall(PATTERN, line)), None) for line in file])
		cards = [(strToSet(card[0]), strToSet(card[1])) for card in cards]
		return cards

def partOne(cards):
	totalPoints = 0
	
	for card in cards:
		wins = numWinning(card)
		if wins <= 0:
			continue
		totalPoints += 2 ** (wins - 1)
	
	return totalPoints

def partTwo(cards):
	consider = [1] * len(cards)
	
	for ind, card in enumerate(cards):
		numExtra = numWinning(card)
		for i in range(numExtra):
			consider[i + ind + 1] += consider[ind]
	
	return sum(consider)

if __name__ == "__main__":
	cards = parseInput("Day4/input.txt")
	print(f"Part One: {partOne(cards)}")
	print(f"Part Two: {partTwo(cards)}")