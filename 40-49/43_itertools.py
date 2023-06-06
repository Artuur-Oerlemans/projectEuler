import itertools
import timeit

start = timeit.default_timer()
# print(list(
#     itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# ))

print(list(reversed(range(10))))
stop = timeit.default_timer()

print('Time:', stop - start, 's')