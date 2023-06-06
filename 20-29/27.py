import math

primes = [2]
i = 3
while len(primes) < 400001:
	prime = True
	j = 0
	while prime and j < len(primes) and primes[j] <= math.sqrt(i):
		if i % primes[j] == 0:
			prime = False
		j += 1

	if prime:
		primes.append(i)
	i += 1

def isPrime(n):
	for p in primes:
		if n < p:
			return False
		elif n ==p:
			return True

print("primes calculated")
bestA = -100000
bestB = -100000
bestSpree = -1

for b in range(0,10001):
	if isPrime(b):
		for a in range(-10000,10001):
	
			spree = 0
			n = 0
			while isPrime(n**2 + a*n + b):
				spree +=1
				n+=1
			if spree > bestSpree:
				bestA = a
				bestB = b
				bestSpree = spree
	if b %100==0:
		print(str(b))

print(bestA*bestB)
