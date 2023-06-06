

primes = [2]
i = 3

while i < 1000000:
	prime = True
	j = 0
	while prime and j < len(primes) and primes[j]*primes[j] <= i:
		if i % primes[j] == 0:
			prime = False
		j += 1

	if prime:
		primes.append(i)
	i += 1
print("done calculating primes")
def isPrime(n):
	return n in primes

numberOfCircularPrimes = 0

for i in primes:
	stringI = str(i)
	rotations = 1
	allPrime = True
	length = len(stringI)
	while allPrime and rotations < length:
		stringI = stringI[length-1]+stringI[:length-1]
		allPrime = isPrime(int(stringI))
		rotations += 1

	if allPrime:
		numberOfCircularPrimes +=1

print(numberOfCircularPrimes)
