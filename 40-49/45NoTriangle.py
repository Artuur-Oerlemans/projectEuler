import math

matchesFound = 0

# If it's Hexagonal number, then it's also a triangle number.

Pn = 1
Hn = 1

nthP = 1
nthH = 1


def calcPn(nthP):
	return nthP*(3*nthP-1)/2


def calcHn(nthH):
	return nthH*(2*nthH-1)

while matchesFound <= 2:
	if Pn < Hn:
		nthP += 1
		Pn = calcPn(nthP)
		print("Pn =", Pn, "n = ", nthP)
	elif Hn < Pn:
		nthH += 1
		Hn = calcHn(nthH)
		print("Hn =", Hn, "n = ", nthH)
	else:
		matchesFound += 1
		print("Match found:", Hn)
		nthH += 1
		Hn = calcHn(nthH)
		print("Hn =", Hn, "n = ", nthH)