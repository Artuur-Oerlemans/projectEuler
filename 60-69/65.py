import math


def calculate_convergent_of_e(nth):
    numerator = 0
    denominator = 1
    for n in range(nth, 1, -1):
        if n % 3 == 0:
            new_div = 2 * (n // 3)
        else:
            new_div = 1

        new_numerator = denominator
        new_denominator = new_div * denominator + numerator
        greatest_common_denominator = math.gcd(new_numerator, new_denominator)
        numerator = new_numerator // greatest_common_denominator
        denominator = new_denominator // greatest_common_denominator

    new_numerator = numerator + 2 * denominator
    new_denominator = denominator
    greatest_common_denominator = math.gcd(new_numerator, new_denominator)
    numerator = new_numerator // greatest_common_denominator
    denominator = new_denominator // greatest_common_denominator
    return numerator, denominator


num, den = calculate_convergent_of_e(100)
print(num)
print(sum([int(x) for x in str(num)]))
