import math
bino = {}
def binomial(t,b):
	if b > t/2:
		b= t-b
	if (t,b) in bino:
		return bino[(t,b)]

	if b==0 or t==b:
		bino[(t,b)] = 1
	elif b==1 or b==t-1:
		bino[(t,b)] = t
	else:
		bino[(t,b)] = binomial(t-1, b) + binomial(t-1, b-1)
	return bino[(t,b)]
print(binomial(40,20))

def factorial(i):
	result = 1
	for j in range(1,i+1):
		result *= j
	return result
print(factorial(40)/factorial(20)/factorial(20))



result = 1
for i in range(1,21):
	result *= (2*i-1) *(2*i)
	result /= i*i
print(result)

