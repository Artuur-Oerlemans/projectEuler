import timeit

start = timeit.default_timer()

sum_pandigitals_with_property = 0


def permutate_first_k_items(items, k):
	if k == 1:
		if has_sub_integer_divisibility_property(items):
			add_to_score(items)
		return

	permutate_first_k_items(items, k - 1)

	for i in range(k - 1):
		if k % 2 == 0:
			items[i], items[k - 1] = items[k - 1], items[i]
		else:
			items[0], items[k - 1] = items[k - 1], items[0]
		permutate_first_k_items(items, k - 1)


def has_sub_integer_divisibility_property(a):
	return (int(a[7] + a[8] + a[9]) % 17 == 0
			and int(a[6] + a[7] + a[8]) % 13 == 0
			and int(a[5] + a[6] + a[7]) % 11 == 0
			and int(a[4] + a[5] + a[6]) % 7 == 0
			and int(a[5]) % 5 == 0
			and int(a[2] + a[3] + a[4]) % 3 == 0
			and int(a[3]) % 2 == 0
			)


def add_to_score(items):
	global sum_pandigitals_with_property
	pandigital = int(''.join(items))
	sum_pandigitals_with_property += pandigital
	print(pandigital)


all_items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
permutate_first_k_items(all_items, len(all_items))

print('result', sum_pandigitals_with_property)

stop = timeit.default_timer()

print('Time:', stop - start, 's')
