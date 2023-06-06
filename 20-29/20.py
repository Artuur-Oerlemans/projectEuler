result = 1
for i in range(1,101):
	result *= i
string = str(result)

output = 0
for i in string:
	output += int(i)
print(output)