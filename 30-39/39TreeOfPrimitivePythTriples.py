import math

maxP = 1000000

rightAngleTrianglesPerPerimeter ={}


def updatePerimeterCounts(p):
	if p in rightAngleTrianglesPerPerimeter:
		rightAngleTrianglesPerPerimeter[p] += 1
	else:
		rightAngleTrianglesPerPerimeter[p] = 1

# If you have the perimeter of a primitive Pythagorean triple, than also multiples of it are perimiters of Pythagorean triples.
def updateScalarPerimeterCounts(p):
	scalarP = p
	while scalarP <= maxP:
		updatePerimeterCounts(scalarP)
		scalarP += p

def recursivePrimitivePerimeterCreator(a,b,c):
	p = a + b + c
	if p > maxP:
		return
	updateScalarPerimeterCounts(p)

	recursivePrimitivePerimeterCreator(a-2*b+2*c, 2*a-b+2*c, 2*a-2*b+3*c)
	recursivePrimitivePerimeterCreator(a+2*b+2*c, 2*a+b+2*c, 2*a+2*b+3*c)
	recursivePrimitivePerimeterCreator(-a+2*b+2*c, -2*a+b+2*c,-2*a+2*b+3*c)

recursivePrimitivePerimeterCreator(3,4,5)

mostTriangles = 0
pWithMostTriangles = 0

for p, triangles in rightAngleTrianglesPerPerimeter.items():
	if triangles > mostTriangles:
		pWithMostTriangles = p
		mostTriangles = triangles

print("The perimeter", pWithMostTriangles, "has", mostTriangles, "right angle triangles with integer sides.")