vector = [0,1,2,3,4,5,6,7,8,9]
#vector = [0,1,2]

numberOfPermutations = 0


def switch(i,j):
	mem = vector[i]
	vector[i] = vector[j]
	vector[j] = mem

def addPerm():
	global numberOfPermutations
	numberOfPermutations +=1
	#print(vector)
	if numberOfPermutations == 1000000-1:
		print(vector)

def permute(begin, length):
	if begin == length-1:
		return
	else:
		numbers = vector[begin:length]
		numbers.sort()
		permute(begin +1, length)
		for i in range(1,len(numbers)):
			k = 1
			for j in numbers:
				if numbers[i] ==j:
					vector[begin] = j
				else:
					vector[begin +k] = j
					k+= 1
			addPerm()

			permute(begin +1, length)



		vector[begin]

permute(0,10)