import math
aPlusB = 1000
searching = True
while aPlusB > 0 and searching:
	c = 1000 - aPlusB
	for b in range(math.ceil(aPlusB/2 + 0.5),c):
		a = aPlusB -b
		if a*a + b*b -c*c == 0:
			print(a*b*c)
			print(a)
			print(b)
			print(c)
			searching = False
	aPlusB -= 1