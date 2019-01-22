import math

def squareRoot(x):
	low = 0.0
	high = float(x+1)
	while (high - low) > 0.000001:
		mid = (low + high) / 2
		if mid*mid < x:
			low = mid
		else:
			high = mid
	return low


print(squareRoot(4))
print(squareRoot(6))
print(squareRoot(9))
print(squareRoot(100))



