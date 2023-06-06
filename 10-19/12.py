import math
minimumDivisor = 500

primes = [2]
i = 3
while len(primes) < 1500:
	prime = True
	j = 0
	while prime and j < len(primes) and primes[j] <= math.sqrt(i):
		if i % primes[j] == 0:
			prime = False
		j += 1

	if prime:
		primes.append(i)
	i += 1

def timesDivisible(n, by):
	times = 0
	while n % by == 0:
		times += 1
		n= n / by
	return times

def phiImporved(n):
	numberOfDivisors = 1
	i=0
	check = True
	while primes[i]<= n:
		if n % primes[i] ==0:
			timesDivisibleBy = timesDivisible(n,primes[i])
			numberOfDivisors *= timesDivisibleBy+1
			n /= primes[i]**timesDivisibleBy

		i+=1

	return numberOfDivisors

def phi(n):
	numberOfDivisors = 0
	for i in range(1, math.ceil(math.sqrt(n))):
		if n % i == 0:
			numberOfDivisors += 1
	numberOfDivisors *= 2
	if math.sqrt(n) == math.ceil(math.sqrt(n)):
		numberOfDivisors += 1
	return numberOfDivisors

def triangleNumberDivisors(nth):
	if nth % 2 ==0:
		return phi(nth/2)*phi(nth+1)
	else:
		return phi(nth)*phi((nth+1)/2)

i = 1
while triangleNumberDivisors(i) <= minimumDivisor:
	i +=1
print(i*(i+1)/2)


