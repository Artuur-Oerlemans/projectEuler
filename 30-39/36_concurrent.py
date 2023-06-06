import multiprocessing as mp

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

def collectPalindromeRange(max, start = 1, step = 2):
	result = []
	for i in range(start, max , step):
		if isBinDecPalindrome(i):
			result.append(i)
	return result

def collect_result(result):
    global results
    results.extend(result)

if __name__ == "__main__":
	maximum = 100000000
	results = []
	pool = mp.Pool(mp.cpu_count())

	step = mp.cpu_count()

	for index in range(0,step , 1):
		pool.apply_async(collectPalindromeRange, args=(maximum, index*2+1, step *2), callback=collect_result) 

	pool.close()
	pool.join()

	print(sum(results))