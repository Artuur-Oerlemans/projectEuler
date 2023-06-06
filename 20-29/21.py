properDivisors = {}
sumAmicable = 0
for i in range(1,10000):
	d = 0
	for j in range(1,i):
		if i %j ==0:
			d += j

	if d in properDivisors.keys() and properDivisors[d] == i:
		sumAmicable += i+d
	properDivisors[i] = d
print(str(sumAmicable))
