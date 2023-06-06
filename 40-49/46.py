import math

max_prime = 1000000

primes_set = set(range(2, max_prime))
for i in range(2, round(math.sqrt(max_prime)) + 1):
    if i in primes_set:
        primes_set.difference_update((i * k for k in range(2, max_prime // i + 1)))
primes = list(primes_set)


def is_prime(n):
    return n in primes_set


def is_square(n):
    root = math.sqrt(n)
    return int(root + 0.5) ** 2 == n


for i in range(9, max_prime, 2):
    if i in primes_set:
        continue
    j = 0
    goldbach_match = False
    while not goldbach_match and primes[j] < i:
        without_prime = i - primes[j]
        if without_prime % 2 == 0:
            goldbach_match = is_square(without_prime // 2)
        j += 1
    if not goldbach_match:
        print("found it, it is", i)
        break
print("done")
