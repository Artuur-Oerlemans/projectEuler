def find_digits_that_up_to(summ, number_max, mem):
    if summ == 0:
        print(mem)
        return 1
    counter = 0
    for i in range(1, min(summ, number_max) + 1):
        mem_copy = mem.copy()
        mem_copy.append(i)
        counter += find_digits_that_up_to(summ - i, min(i, number_max), mem_copy)
    return counter


print(find_digits_that_up_to(100, 99, []))
