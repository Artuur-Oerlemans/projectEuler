import math
n=10_000_000

primes = set(range(2,n))
for i in range(2,round(math.sqrt(n))+1):
    if i in primes:
        primes.difference_update((i*k for k in range(2,n//i+1)))

def isPrime(n):
	return n in primes

def isPandigital(n):
	nString = str(n)
	digits = set(nString)
	if len(nString) == len(digits):
		for i in range(1, len(nString)+1):
			if str(i) not in digits:
				return False
		return True

highestPandigitalPrime = 0

for p in primes:
	if isPandigital(p) and p > highestPandigitalPrime:
		print(p)
		highestPandigitalPrime = p