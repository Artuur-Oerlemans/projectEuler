file = open("p022_names.txt","r")
contents = file.read()
nameArray = contents[1:-1].split('","')
nameArray.sort()

def scoreName(name):
	result = 0
	for k in name:
		result += ord(k)-64
	return result

score = 0
for i in range(1, len(nameArray)+1):
	score += i * scoreName(nameArray[i-1])
print(score)
