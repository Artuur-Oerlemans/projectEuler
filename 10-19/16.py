import math
result = 0
twothousand = str(2**1000)
for i in twothousand:
	result += int(i)
print(result)


power = 1000
prod = 1
memory = 2
while power != 0:
	if power % 2 != 0:
		power -=1
		prod *= memory
	power /= 2
	memory *= memory
twothousand = str(prod)
result = 0
for i in twothousand:
	result += int(i)
print(result)

power = 1000
prod = 1
memory = 2
while power != 0:
	if power % 2 != 0:
		power -=1
		prod *= memory
	power /= 2
	memory *= memory
twothousand = str(prod)
result = 0
for i in twothousand:
	result += int(i)
print(result)


power = 1000
prod = {0: 1}
memory = {0:2}
while power != 0:
	if power % 2 != 0:
		power -=1
		prod *= memory
	power /= 2
	memory *= memory
twothousand = str(prod)
result = 0
for i in twothousand:
	result += int(i)
print(result)
