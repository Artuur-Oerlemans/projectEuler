import math

max_prime = 1000000

primes_set = set(range(2, max_prime))
for i in range(2, round(math.sqrt(max_prime)) + 1):
    if i in primes_set:
        primes_set.difference_update((i * k for k in range(2, max_prime // i + 1)))


def is_prime(n):
    if n > max_prime:
        print("too few primes")
    return n in primes_set
