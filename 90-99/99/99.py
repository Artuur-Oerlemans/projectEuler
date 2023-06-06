file = open("p099_base_exp.txt", "r")
contents = file.read()
pairs = [[int(s) for s in line.split(',')] for line in contents.split('\n')]

highest_value = 0
line = -1
for i in range(0, len(pairs)):
    print(i)
    pair = pairs[i]
    value = pair[0] ** pair[1]
    if value > highest_value:
        highest_value = value
        line = i + 1

print(line)

