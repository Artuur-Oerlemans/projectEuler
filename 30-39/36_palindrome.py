import multiprocessing as mp



def collectPalindromeFromRange(max, start = 1, step = 1):
	result = []
	for i in range(start, max , step):
		for odd in [True, False]:
			palin = makePalindrome(i, odd)
			if isBinDecPalindrome(palin):
				result.append(palin)
	return result

def makePalindrome(i, odd):
	palin = i
	remainder = i 
	if odd:
		remainder = remainder // 10

	while remainder >0:
		palin = palin * 10 + (remainder % 10)
		remainder = remainder // 10
	return palin


def isBinDecPalindrome(i):
	iBinary = "{0:b}".format(i)
	return isPalindrome(str(i)) and isPalindrome(iBinary)

def isPalindrome(string):
	length = len(string)
	palindrome = True
	i=0
	while palindrome and i<length//2:
		palindrome = string[i] == string[length-i-1]
		i+=1
	return palindrome

def collect_result(result):
    global results
    results.extend(result)

if __name__ == "__main__":
	maximum = 10000
	results = []
	pool = mp.Pool(mp.cpu_count())

	step = mp.cpu_count()

	for index in range(0,step , 1):
		pool.apply_async(collectPalindromeFromRange, args=(maximum, index+1, step), callback=collect_result) 

	pool.close()
	pool.join()

	print(sum(results))