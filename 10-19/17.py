
irregularNumbers ={1: "one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	10:"ten",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen",
	15:"fifteen",
	16:"sixteen",
	17:"seventeen",
	18:"eighteen",
	19:"nineteen"
	}

tensStrings = {20:"twenty",
	30:"thirty",
	40:"forty",
	50:"fifty",
	60:"sixty",
	70:"seventy",
	80:"eighty",
	90:"ninety"
	}

def getString(n):
	result = ""

	if n <20:
		result = irregularNumbers[n]

	elif n < 100:
		lastDigit = n%10
		tens = (n - lastDigit)
		result += tensStrings[tens]
		if lastDigit !=0:
			result+= getString(lastDigit)

	elif n < 1000:
		lastTwo = n % 100
		hunderdDigit = (n - lastTwo)/100

		result += getString(hunderdDigit) + "hundred"
		if lastTwo != 0:
			result += "and" + getString(lastTwo)
	else:
		result = "onethousand"
	return result

allNumbers = ""
for n in range(1,1001):
	allNumbers+= getString(n)
	print(getString(n))
print(len(allNumbers))


