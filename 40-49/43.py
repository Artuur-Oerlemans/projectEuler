import timeit

start = timeit.default_timer()
# 7.6 seconds for all pandigitals


def get_all_permutations(items: list):
    if len(items) == 1:
        return items

    all_permutations = list()

    for first in items:
        rest = items.copy()
        rest.remove(first)
        for suffix in get_all_permutations(rest):
            all_permutations.append(first + suffix)
    return all_permutations


get_all_permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
# print(
#     # get_all_permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
#     get_all_permutations(["1", "2", "3"])
# )

stop = timeit.default_timer()

print('Time:', stop - start, 's')


