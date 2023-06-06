
def isPalindrome(string):
	length = len(string)
	palindrome = True
	i=0
	while palindrome and i<length//2:
		palindrome = string[i] == string[length-i-1]
		i+=1
	return palindrome

def isBinDecPalindrome(i):
	iBinary = "{0:b}".format(i)
	return isPalindrome(str(i)) and isPalindrome(iBinary)

def collectPalindromeRange(max, step = 2, start = 1):
	result = []
	for i in range(start, max , step):
		if isBinDecPalindrome(i):
			result.append(i)
	return result

if __name__ == "__main__":
	print(sum(collectPalindromeRange(10000000)))