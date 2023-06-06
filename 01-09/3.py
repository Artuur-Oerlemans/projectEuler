import math
def largestPrimeDivisor(n):
	for x in range(2,round(math.sqrt(n))+1):
		if n%x ==0:
			return max(largestPrimeDivisor(n/x),x)
	return n
print(largestPrimeDivisor(600851475143))
