import math

primes = [2]
i = 3
while len(primes) < 10001:
	prime = True
	j = 0
	while prime and j < len(primes) and primes[j] <= math.sqrt(i):
		if i % primes[j] == 0:
			prime = False
		j += 1

	if prime:
		primes.append(i)
	i += 1
print(primes[10000])