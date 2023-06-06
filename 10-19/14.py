collatzLength = []
upperbound = 1000000
for x in range(0,upperbound):
	collatzLength.append(-1)


def nextCollatz(i):
	if i % 2==0:
		return int(i/2)
	else:
		return 3*i+1


def calcLength(i):
	if i >= upperbound:
		return calcLength(nextCollatz(i))+1

	if collatzLength[i] != -1:
		return collatzLength[i]
	if i ==1:
		return 1
	else:
		collatzLength[i] = calcLength(nextCollatz(i))+1
	return collatzLength[i]

longest = 1
startingPointLongest = -1
for i in range(int(upperbound/2),upperbound):
	if calcLength(i) > longest:
		longest = calcLength(i)
		startingPointLongest = i

print(startingPointLongest)