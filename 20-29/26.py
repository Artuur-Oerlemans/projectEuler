

def divide(den, num, digits):
	if digits <=0:
		return ""
	times = 0 
	while(den <= num):
		times += 1
		num -= den

	return str(times) + divide(den, num * 10, digits -1)

def recursionCounter(den, num, knownNum):
	num = num % den
	if (num in knownNum):
		return(len(knownNum) - knownNum.index(num))
	else:
		knownNum.append(num)
		return recursionCounter(den, num * 10, knownNum)


lengthLongestCycle = 1
longestCycle = 0
for d in range(2,1000):
	length = recursionCounter(d,1,[])
	if(length > lengthLongestCycle):
		lengthLongestCycle = length
		longestCycle = d
print(str(longestCycle))
