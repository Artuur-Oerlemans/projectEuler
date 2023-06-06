import math


def concat_multiples(n, till):
    concatenated = ""
    for i in range(1, till):
        concatenated += str(n * i)
    return int(concatenated)


def is_pandigital(n):
    n_string = str(n)
    digits = set(n_string)
    if len(n_string) == len(digits):
        for i in range(1, len(n_string) + 1):
            if str(i) not in digits:
                return False
        return True


highest_concatenated_pandigital = 0
multiplier = 9

for i in range(1, 10000):
    concatenated_product = concat_multiples(i, multiplier)
    while len(str(concatenated_product)) > 9:
        multiplier -= 1
        concatenated_product = concat_multiples(i, multiplier)

    if is_pandigital(concatenated_product) and concatenated_product > highest_concatenated_pandigital:
        highest_concatenated_pandigital = concatenated_product
        print(concatenated_product)

print("The highest concatenated products that is a pandigital number is:", highest_concatenated_pandigital)
