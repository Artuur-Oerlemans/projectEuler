result =1
to = 20
for x in range(2,to+1):
	if result % x != 0:
		prod = x
		while prod <= to:
			result *= x
			prod *= x
print(result)