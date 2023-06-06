import math

def concatMultiples(n, until):
	concatenated = ""
	for i in range(1, until +1):
		concatenated += str(n * i)
	return int(concatenated)

def isPandigital(n):
	nString = str(n)
	digits = set(nString)
	if len(nString) == len(digits):
		for i in range(1, len(nString)+1):
			if str(i) not in digits:
				return False
		return True

highestConcatenatedPandigital = 0

# Because of the example we know it should start with a 9.
# Futhermore it's only possible to get 9 digits if use the number 9 (example) or a 4-digit number.
multiplier = 2
for i in range(9123, 10000):
	concatenatedProduct = concatMultiples(i, multiplier)

	if isPandigital(concatenatedProduct) and concatenatedProduct > highestConcatenatedPandigital:
		highestConcatenatedPandigital = concatenatedProduct
		print(concatenatedProduct)

print("The highest concatenated products that is a pandigital number is:", highestConcatenatedPandigital)