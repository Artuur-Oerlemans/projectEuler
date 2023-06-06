import math
maxi=1000000

primes = set(range(2,maxi))
for i in range(2,round(math.sqrt(maxi))+1):
    if i in primes:
        primes.difference_update((i*k for k in range(2,maxi//i+1)))

primesList = list(primes)

# We want to maximize the value of n/phi(n) with phi(n) being the number of relative primes to n.
# The strategy I'm going to try is maximizing n while minimizing phi(n). 
# Observation: phi(n) is particularly small when n is a multiple of small distinct primes.
# You can further more prove this using the properties of phi(), which include
# phi(p^n)=p^(n-1)phi(p) and a trick for multiplying numbers made from different primes
i = 0
productOfPrimes = 1

while productOfPrimes * primesList[i] < 1_000_000:
	productOfPrimes *= primesList[i]
	i+=1

print(productOfPrimes)