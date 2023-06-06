highest_sum = 1


def calc_digit_sum(n):
    sum_n = 0
    for s in str(n):
        sum_n += int(s)
    return sum_n


for i in range(1, 100):
    for j in range(1, 100):
        sum_i_j = calc_digit_sum(i ** j)
        if sum_i_j > highest_sum:
            highest_sum = sum_i_j
            print(sum_i_j)
