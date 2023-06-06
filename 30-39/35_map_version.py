import math
import multiprocessing as mp


def isCircularPrime(i, primes):
	stringI = str(i)
	rotations = 1
	allPrime = True
	length = len(stringI)
	while allPrime and rotations < length:
		stringI = stringI[length-1]+stringI[:length-1]
		allPrime = int(stringI) in primes
		rotations += 1

	return allPrime



def circularPrimesWithSteps(index, step, listPrimes, primes):
	found = 0
	l = len(listPrimes)
	while index < l:
		if isCircularPrime(listPrimes[index], primes):
			found+= 1
		index += step
	return found

def collect_result(result):
    global results
    results.append(result)

if __name__ == "__main__":

	n=10000000

	primes = set(range(2,n))
	for i in range(2,round(math.sqrt(n))+1):
	    if i in primes:
	        primes.difference_update((i*k for k in range(2,n//i+1)))

	print("done calculating primes")

	results = []
	step = mp.cpu_count()

	pool = mp.Pool(mp.cpu_count())

	listPrimes = list(primes)

	for index in range(0,step):
		pool.apply_async(circularPrimesWithSteps, args=(index,step,listPrimes, primes), callback=collect_result) 

	pool.close()
	pool.join()


	print(sum(results))