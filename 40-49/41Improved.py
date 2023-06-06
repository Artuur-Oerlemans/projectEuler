import math

def isPrime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i+=1
	return True

def isPandigital(n):
	nString = str(n)
	digits = set(nString)
	if len(nString) == len(digits):
		for i in range(1, len(nString)+1):
			if str(i) not in digits:
				return False
		return True

possiblePP = 7654321

while not (isPandigital(possiblePP) and isPrime(possiblePP)) and possiblePP >0:
	possiblePP -= 2

print("biggest PP", possiblePP)