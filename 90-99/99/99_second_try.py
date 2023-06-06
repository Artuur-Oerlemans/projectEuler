file = open("p099_base_exp.txt", "r")
contents = file.read()
pairs = [[int(s) for s in line.split(',')] for line in contents.split('\n')]

lines_and_pairs = []
for i in range(0, len(pairs)):
    line = i
    pair = pairs[i]
    lower_value = False
    for other_pair in pairs:
        if pair[0] < other_pair[0] and pair[1] < other_pair[1]:
            lower_value = True
            break
    if not lower_value:
        lines_and_pairs.append((line, pair))

# this method only removed 16 pairs, highly disappointing
print("new number of possible pairs that can have the highest value", len(lines_and_pairs), "out of a 1000")


# highest_value = 0
# highest_line = -1
# for i in range(0, len(pairs)):
#     print(i)
#     pair = pairs[i]
#     value = pair[0] ** pair[1]
#     if value > highest_value:
#         highest_value = value
#         line = i + 1
#
# print(line)
