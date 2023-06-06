wordsFile = open("42_words.txt","r")
wordsString = wordsFile.read()
words = wordsString.split('","')

triangleNumbers = set([x*(x+1)/2 for x in range(200)])

def isTriangle(word):
	value = 0
	for l in word:
		value += ord(l) - ord('A')+1
	return value in triangleNumbers


triangleWords = []
for word in words:
	if isTriangle(word):
		triangleWords.append(word)

print(len(triangleWords))
print(isTriangle("A"))