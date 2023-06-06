from queue import PriorityQueue
import math

max_prime = 200000000

primes_set = set(range(2, max_prime))
for i in range(2, round(math.sqrt(max_prime)) + 1):
    if i in primes_set:
        primes_set.difference_update((i * k for k in range(2, max_prime // i + 1)))
primes = sorted(list(primes_set))
print("calculated primes")


def is_prime(n):
    # if n > max_prime:
    #     print("too few primes")
    return n in primes_set


DESIRED_NUMBER = 5


def calc_minimum_value(coll, prime_index):
    minimum_value = sum(coll)
    for n in range(0, DESIRED_NUMBER - len(coll)):
        minimum_value += primes[prime_index + 1 + n]
    return minimum_value


def all_concat_prime(coll, new_prime):
    for p in coll:
        if not is_prime(int(str(p) + str(new_prime))) or not is_prime(int(str(new_prime) + str(p))):
            return False
    return True


def find_lowest_sum_of_primes_that_concat_to_primes():
    pq = PriorityQueue()

    for prime_index in range(1, 100):
        coll = [primes[prime_index]]
        minimum_value = calc_minimum_value(coll, prime_index)
        pq.put((minimum_value, (coll, prime_index)))

    lowest_score = 999999999999999999999999

    minimum_value, (coll, prime_index) = pq.get()
    while minimum_value < lowest_score:
        new_minimum_value = calc_minimum_value(coll, prime_index + 1)
        pq.put((new_minimum_value, (coll.copy(), prime_index + 1)))

        if all_concat_prime(coll, primes[prime_index + 1]):
            new_coll = coll.copy()
            new_coll.append(primes[prime_index + 1])
            new_minimum_value = calc_minimum_value(new_coll, prime_index + 1)
            if len(new_coll) == DESIRED_NUMBER:
                print(new_coll)
                if new_minimum_value < lowest_score:
                    lowest_score = new_minimum_value
            else:
                pq.put((new_minimum_value, (new_coll, prime_index + 1)))
            # if len(new_coll) == DESIRED_NUMBER - 1:
            #     print(new_coll)

        minimum_value, (coll, prime_index) = pq.get()
    return lowest_score


print(find_lowest_sum_of_primes_that_concat_to_primes())
