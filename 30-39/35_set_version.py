import math

n=10000000

primes = set(range(2,n))
for i in range(2,n//2+1):
    if i in primes:
        primes.difference_update((i*k for k in range(2,n//i+1)))

print("done calculating primes")
def isPrime(n):
	return n in primes

numberOfCircularPrimes = 0

listPrimes = list(primes)

for i in listPrimes:
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
