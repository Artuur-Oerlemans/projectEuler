import math

def sameDigitsTimes(n , times):
	setN = set(str(n))
	setTimes = set(str(n * times))

	return setN == setTimes

def sameDigitsTimes2toX(n, x):
	for times in range(2,x):
		if not sameDigitsTimes(n , times):
			return False
	return True


def addPrefixOne(suffix):
	return int("1" + str(suffix))


sameDigitsFound = False

possibleEndDigits = 1

while not sameDigitsFound:
	possibleEndDigits +=1

	possibleSameDigits = addPrefixOne(possibleEndDigits)
	sameDigitsFound = sameDigitsTimes2toX(possibleSameDigits, 7)

print("Smallest same digits: ", addPrefixOne(possibleEndDigits))
