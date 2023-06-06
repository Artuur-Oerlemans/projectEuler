import math

largestPalindrome = 0



def isPalindrome(n):
	nString = str(n)
	numberOfDigits = len(nString)
	for i in range(0,math.ceil(numberOfDigits/2)):
		if nString[i] != nString[numberOfDigits-1-i]:
			return False
	return True


for x in range(100,1000):
	for y in range(x,1000):
		if isPalindrome(x*y) and x*y > largestPalindrome:
			largestPalindrome = x*y
			print(x*y)
			print(x)
			print(y)