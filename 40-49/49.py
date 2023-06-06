import math

max_prime = 10000

primes_set = set(range(2, max_prime))
for i in range(2, round(math.sqrt(max_prime)) + 1):
    if i in primes_set:
        primes_set.difference_update((i * k for k in range(2, max_prime // i + 1)))
primes = list(primes_set)
primes.sort()
print("calculated primes")


def is_permutation(a: int, b: int):
    return set(str(a)) == set(str(b))


i = 0
while primes[i] < 1000:
    i += 1

while i < len(primes):
    prime_1 = primes[i]
    for j in range(i + 1, len(primes)):
        prime_2 = primes[j]
        if is_permutation(prime_1, prime_2):
            prime_3 = prime_2 + prime_2 - prime_1
            if prime_3 in primes_set and is_permutation(prime_1, prime_3):
                print(prime_1, prime_2, prime_3)
    i += 1
