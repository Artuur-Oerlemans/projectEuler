def sumProper(k):
	d = 0
	for j in range(1,i):
		if i %j ==0:
			d += j
	return d

abundantNumbers = []
#for i in range(1, 28124):
#	if i < sumProper(i):
#		abundantNumbers.append(i)

sumPropers = {}
for i in range(1,28123+1):
	sumPropers[i] = 0

for i in range(1,12070):
	j = 2
	while i*j <= 28123:
		sumPropers[i*j] += i
		j+= 1

for i in range(1,28123+1):
	if sumPropers[i] > i:
		abundantNumbers.append(i)
		sumPropers[i] = True
	else:
		sumPropers[i] = False

result =0

for i in range(1,28123+1):
	isSum = False
	j=1
	while (not isSum and j < i):
		isSum = sumPropers[j] and sumPropers[i-j]
		j+= 1
	if not isSum:
		result +=i


print(result)