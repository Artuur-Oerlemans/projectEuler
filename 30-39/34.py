import math

result = 0
for n in range(3,2177282):
	sumationFactorialDigits = 0
	for digit in str(n):
		sumationFactorialDigits += math.factorial(int(digit))

	if sumationFactorialDigits == n:
		print(n)
		result +=n

print(result)


