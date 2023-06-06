import math
import functools

max_prime = 10000000

primes_set = set(range(2, max_prime))
for m in range(2, round(math.sqrt(max_prime)) + 1):
    if m in primes_set:
        primes_set.difference_update((m * k for k in range(2, max_prime // m + 1)))
primes = list(primes_set)
primes.sort()
print("calculated primes")


@functools.cache
def get_mask_masks(length):
    masks = []
    for i in range(1, 2 ** length):
        string_mask = format(i, "b").zfill(length)
        mask = []
        for j in range(0, len(string_mask)):
            mask.append(string_mask[j] == '1')
        masks.append(mask)
    return masks


def get_sub_masks(base_mask):
    places = 0
    for i in range(0, len(base_mask)):
        if base_mask[i]:
            places += 1
    mask_masks = get_mask_masks(places)
    sub_masks = []
    for mask_mask in mask_masks:
        used = 0
        mask = []
        for pos in range(0, len(base_mask)):
            if base_mask[pos]:
                mask.append(mask_mask[used])
                used += 1
            else:
                mask.append(False)
        sub_masks.append(mask)
    return sub_masks


def get_masks(p):
    str_p = str(p)
    masking_values = set(str_p)
    masks = []
    for mv in masking_values:
        # can't have 8 primes if the last digit is even half of the time
        base_mask = []
        for i in range(0, len(str_p) - 1):
            base_mask.append(str_p[i] == str(mv))
        base_mask.append(False)
        sub_masks = get_sub_masks(base_mask)
        masks.extend(sub_masks)
    return masks


def get_possible_numbers(p: int, mask: list[bool]):
    str_p = str(p)
    str_possible_numbers = ["" for x in range(0, 10)]
    for pos in range(0, len(str_p)):
        if mask[pos]:
            for i in range(0, 10):
                str_possible_numbers[i] = str_possible_numbers[i] + str(i)
        else:
            for i in range(0, 10):
                str_possible_numbers[i] = str_possible_numbers[i] + str_p[pos]
    if str_possible_numbers[0][0] == "0":
        str_possible_numbers.pop(0)
    # if p == 13:
    #     print(str_possible_numbers)
    return [int(x) for x in str_possible_numbers]


def find_solution():
    for p in primes:
        masks = get_masks(p)
        for mask in masks:
            possible_numbers = get_possible_numbers(p, mask)
            number_of_primes = 0
            for n in possible_numbers:
                if n in primes_set:
                    number_of_primes += 1
            if number_of_primes >= 8:
                return p


print("found solution", find_solution())
