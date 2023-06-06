import math
print("hello, world")
result = 0
for x in range(1,1000):
	if x%3==0 or x%5==0:
		result += x
print(result)

def sumMultiples(of, maxi):
	terms = math.floor(maxi/of)
	return terms*(terms+1)/2*of
print(sumMultiples(3,999)+sumMultiples(5,999)-sumMultiples(15,999))