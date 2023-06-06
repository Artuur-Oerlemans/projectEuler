import math
numberOfPrimes=10000000

primes = set(range(2,numberOfPrimes))
for i in range(2,round(math.sqrt(numberOfPrimes))+1):
    if i in primes:
        primes.difference_update((i*k for k in range(2,numberOfPrimes//i+1)))

def isPrime(n):
	return n in primes

truncatablePrimes = set()
intruncatablePrimes = {2,3,5,7}

def isRightTruncatable(n):
	trunc = rightTruncate(n)
	if(isPrime(trunc)):
		if(digits(trunc) == 1):
			return True
		else:
			return isRightTruncatable(trunc)
	return False

def isLeftTruncatable(n):
	trunc = leftTruncate(n)
	if(isPrime(trunc)):
		if(digits(trunc) == 1):
			return True
		else:
			return isLeftTruncatable(trunc)
	return False

def rightTruncate(n):
	return math.floor(n/10)

def leftTruncate(n):
	return n % 10 ** (digits(n) - 1)

def digits(n):
	return int(math.log10(n)) + 1

for i in primes:
	if(isLeftTruncatable(i) and isRightTruncatable(i)):
		truncatablePrimes.add(i)

print(truncatablePrimes)
print(sum(truncatablePrimes))
