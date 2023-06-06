productNumerators =1
productDenominators =1

def check(n1,d1,n2,d2):
	if int(n1)*int(d2) == int(n2)*int(d1):
		global productNumerators
		global productDenominators
		productNumerators *= int(n2)
		productDenominators *= int(d2)


for num in range(10,99):
	for den in range(num+1,99):
		numString = str(num)
		denString = str(den)
		for digitNum in range(0,2):
			for digitDen in range(0,2):
				if numString[digitNum] == denString[digitDen] and den % 10 != 0 and num % 10 != 0:
					check(num,den,numString[1-digitNum],denString[1-digitDen])

print(productNumerators)
print(productDenominators)

