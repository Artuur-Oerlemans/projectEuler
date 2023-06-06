first = 1
second = 2
result = 0

while second <=4000000:
	result+= second
	newSecond = 3*second + 2*first
	first = newSecond- second - first
	second = newSecond

print(result)







first = 2
second = 8
summation = first

while second <=4000000:
	summation += second
	newTerm = 4*second+first
	first = second
	second = newTerm

print(summation)

