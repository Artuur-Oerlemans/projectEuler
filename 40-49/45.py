import math

matchesFound = 0

Tn = 1
Pn = 1
Hn = 1

nthT = 1
nthP = 1
nthH = 1

def calcTn(nthT):
	return nthT*(nthT+1)/2


def calcPn(nthP):
	return nthP*(3*nthP-1)/2


def calcHn(nthH):
	return nthH*(2*nthH-1)

while matchesFound <= 2:
	if Tn < Pn or Tn < Hn:
		nthT += 1
		Tn = calcTn(nthT)
		print("Tn =", Tn, "n = ", nthT)
	elif Pn < Tn or Pn < Hn:
		nthP += 1
		Pn = calcPn(nthP)
		print("Pn =", Pn, "n = ", nthP)
	elif Hn < Tn or Hn < Pn:
		nthH += 1
		Hn = calcHn(nthH)
		print("Hn =", Hn, "n = ", nthH)
	else:
		matchesFound += 1
		print("Match found:", Tn)
		nthH += 1
		Hn = calcHn(nthH)
		print("Hn =", Hn, "n = ", nthH)