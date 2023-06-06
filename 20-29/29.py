a =100
b =100

# doesn't work, because it doesn't keep in mind that 2^5 and 2^6 both give 2^30
# def nonDuplicatePowers(n):
# 	numberOfPowers = 0
# 	inValidPowers =[]
# 	aboveA = False
# 	for pow in range(2,b+1):
# 		if not aboveA:
# 			if n**pow>a:
# 				aboveA = True
# 			else:
# 				inValidPowers.append(pow)
# 		if notDivisibleBy(pow, inValidPowers) or pow == 2:
# 			numberOfPowers += 1
# 			print(n**pow)
# 	return numberOfPowers

# def notDivisibleBy(p, array):
# 	for d in array:
# 		if p%d==0:
# 			return False
# 	return True 

# numberOfDistinctTerms = 0
# for n in range(2,a+1):
# 	numberOfDistinctTerms += nonDuplicatePowers(n)

# print(numberOfDistinctTerms)

powersUsed = {}
expressedInPowers = {}

for n in range(2,a +1):
	powersUsed[n] = []

	power = 1
	while n**power <=a and n**power not in expressedInPowers.keys():
		expressedInPowers[n**power] = (n, power)
		power += 1

numberOfDistinctTerms = 0

for n in range(2,a+1):
	base = expressedInPowers[n][0]
	log = expressedInPowers[n][1]
	for power in range(2,b+1):
		if power * log not in powersUsed[base]:
			numberOfDistinctTerms += 1
			powersUsed[base].append(power * log)

print(numberOfDistinctTerms)




