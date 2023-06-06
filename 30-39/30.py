sumOfDigitFifthPowers = 0
power = 5

for i in range(2,354294):
	raisedToPowerSummation = 0
	for d in str(i):
		raisedToPowerSummation += int(d)**power

	if raisedToPowerSummation == i:
		print(i)
		sumOfDigitFifthPowers += i

print(sumOfDigitFifthPowers)
