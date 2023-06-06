import math
import functools

max_prime = 1000000

primes_set = set(range(2, max_prime))
for i in range(2, round(math.sqrt(max_prime)) + 1):
    if i in primes_set:
        primes_set.difference_update((i * k for k in range(2, max_prime // i + 1)))
primes = list(primes_set)
primes.sort()
print("calculated primes")


def is_prime(n):
    return n in primes_set


memory = {}


def find_prime_factors(n):
    factors = set()
    remainder = n
    i = 0

    while primes[i] < math.sqrt(remainder) + 1:
        divider = primes[i]
        while remainder % divider == 0:
            remainder = remainder // divider
            factors.add(divider)
            if remainder in memory.keys():
                return factors.union(memory[remainder])
        i += 1
    if remainder != 1:
        factors.add(remainder)
    return factors


def mem_find_prime_factors(n):
    factors = find_prime_factors(n)
    memory[n] = factors
    return factors


found = False
index = 2
wanted_number = 5

while not found and index < max_prime * max_prime:
    i = 0
    while len(mem_find_prime_factors(index + i)) == wanted_number and i < wanted_number:
        if i == wanted_number - 1:
            found = True
            print("found", index)
        # print(index + i, memory[index + i])
        i += 1
    # print(index + i, memory[index + i])
    index += i + 1

