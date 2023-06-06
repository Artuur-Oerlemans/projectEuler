import math
maxPrimes=1000000
lengthMostConsecutive = 1
mostConsecutiveSumPrime = 2

# Calculating all primes less than max primes
primes = set(range(2,maxPrimes))
for i in range(2,round(math.sqrt(maxPrimes))+1):
    if i in primes:
        primes.difference_update((i*k for k in range(2,maxPrimes//i+1)))
primesList = list(primes)

def isPrime(n):
	return n in primes


# Algorithm
startChain = 0
while primesList[startChain] < maxPrimes / lengthMostConsecutive:
	sumConsecutives = primesList[startChain]
	endChain = startChain +1

	while sumConsecutives < maxPrimes and endChain < len(primes):
		endChain += 1
		sumConsecutives += primesList[endChain -1]

		if endChain - startChain > lengthMostConsecutive and isPrime(sumConsecutives):
			lengthMostConsecutive = endChain - startChain
			mostConsecutiveSumPrime = sumConsecutives

	startChain +=1

print("length:", lengthMostConsecutive, "sum:", mostConsecutiveSumPrime, "start:", primesList[startChain])