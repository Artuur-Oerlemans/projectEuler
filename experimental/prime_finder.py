# slow, use the power of sets instead
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
	i += 2
print("done calculating primes")

def isPrime(n):
	return n in primes