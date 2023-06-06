
digits = 0
digitMax = 1000000
i = 1
result = 1
digitsNeeded = [10**j for j in range(0,7)]

while(digits <= digitMax):
	for d in str(i):
		digits+=1
		if digits in digitsNeeded:
			result *= int(d)
	i+=1
print(result)