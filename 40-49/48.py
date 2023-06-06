
summ = 0
mod = 10000000000

for i in range(1,1001):
	summ+= pow(i,i,mod)
print(summ % mod)