def reverse(n):
    return int(str(n)[::-1])


lychrel_counter = 0
for i in range(1, 10_000):
    not_reversed = i
    # apparently 'reversed' is already something build-in in python
    reversed1 = reverse(i)
    for j in range(0, 50):
        not_reversed = not_reversed + reversed1
        reversed1 = reverse(not_reversed)
        # print(not_reversed)
        if not_reversed == reversed1:
            break
        elif j == 49:
            lychrel_counter += 1

print(lychrel_counter)