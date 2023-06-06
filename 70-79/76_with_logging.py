import functools

highest_number = 0


@functools.cache
def find_digits_that_up_to(summ, number_max):
    if summ == 0:
        return 1
    counter = 0
    for i in range(1, min(summ, number_max) + 1):
        counter += find_digits_that_up_to(summ - i, min(i, number_max))
    return counter


print(find_digits_that_up_to(100, 99))
