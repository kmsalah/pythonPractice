
#decorators practice


#ax^2 + bx + c
def polynomial_creator(a, b, c):
	def polynomial(x):
		return a * x**2 + b * x + c
	return polynomial


p1 = polynomial_creator(2, 3, 1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
	print(x, p1(x), p2(x))




#arbitary degree polynomial

def polynomial_creator_arb(*coefficients):
	def polynomial(x):
		res = 0
		for index, coeff in enumerate(coefficients):
			res += coeff * x **index
		return res
	return polynomial

print("--------------------------")
p1 = polynomial_creator_arb(4)
p2 = polynomial_creator_arb(2, 4)
p3 = polynomial_creator_arb(2, 3, -1, 8, 1)
p4 = polynomial_creator_arb(-1, 2, 1)

for x in range(-2, 2, 1):
	print(x, p1(x), p2(x), p3(x), p4(x))
