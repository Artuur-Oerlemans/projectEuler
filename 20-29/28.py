suma = 1
add = 1
for i in range(1, 501):
	for j in range(0,4):
		add += 2*i
		suma+= add

print(suma)