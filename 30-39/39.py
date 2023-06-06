import math

maxP = 100000
squares = set(i*i for i in range(1, int(maxP/2)))
rightAngleTrianglesPerPerimeter ={}


def updatePerimeterCounts(a,b,c):
	p = a+b+c
	if p in rightAngleTrianglesPerPerimeter:
		rightAngleTrianglesPerPerimeter[p] += 1
	else:
		rightAngleTrianglesPerPerimeter[p] = 1


for a in range(1, int(maxP/3)+3):
	for b in range(a, int((maxP-a)/2)+1):
		if a*a+b*b in squares:
			c = int(math.sqrt(a*a+b*b))
			if b <= c and a+b+c < maxP:
				updatePerimeterCounts(a,b,c)

mostTriangles = 0
pWithMostTriangles = 0

for p, triangles in rightAngleTrianglesPerPerimeter.items():
	if triangles > mostTriangles:
		pWithMostTriangles = p
		mostTriangles = triangles

print("The perimeter", pWithMostTriangles, "has", mostTriangles, "right angle triangles with integer sides.")