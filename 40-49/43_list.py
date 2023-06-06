import timeit

start = timeit.default_timer()
# 7.6 seconds for all pandigitals


def get_all_permutations_list(items: list):
    if len(items) == 1:
        return [items]

    all_permutations = list()

    for last in items:
        rest = items.copy()
        rest.remove(last)
        for first_part in get_all_permutations_list(rest):
            first_part.append(last)
            all_permutations.append(first_part)
    return all_permutations


get_all_permutations_list(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
# print(
    # get_all_permutations_list(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    # get_all_permutations_list(["1", "2", "3"])
# )

stop = timeit.default_timer()

print('Time:', stop - start, 's')
