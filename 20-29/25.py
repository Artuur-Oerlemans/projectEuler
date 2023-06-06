f1 = 1
f2 = 1
index =2
while(f2 < 10**999):
	mem = f2
	f2 = f1+f2
	f1 = mem
	index +=1
print(index)