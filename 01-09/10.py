import math

primes = [2]
i = 3
while i < 2000000:
	prime = True
	j = 0
	while prime and j < len(primes) and primes[j] <= math.sqrt(i):
		if i % primes[j] == 0:
			prime = False
		j += 1

	if prime:
		primes.append(i)
	i += 1
print(sum(primes))