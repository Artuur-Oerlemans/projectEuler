from itertools import permutations 
import time
t1 = time.time()
perm = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9],5) 


pandigitalProducts = []

def checkPandigital(a, b):
	if len(str(a*b)) != 4:
		return

	# the function set removes duplicates, thus if pandigital there should be no duplicates
	if len(set(str(a)+str(b)+str(a*b)))== 9 and "0" not in str(a*b):
		global pandigitalProducts
		pandigitalProducts.append(a*b)


for i in list(perm): 
    a = i[0]
    b = i[1]*1000 + i[2]*100 + i[3]*10 + i[4]
    checkPandigital(a,b)

    a = i[0] *10 + i[1]
    b = i[2]*100 + i[3]*10 + i[4]
    checkPandigital(a,b)

print(sum(set(pandigitalProducts)))
t2 = time.time()
print(t2 - t1)