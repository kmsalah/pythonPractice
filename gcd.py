def gcd(num1, num2):
	def helper(a, b):
		R = a%b
		if R == 0:
			return b
		else:
			return helper(b, R)
	return helper(num1, num2)

print(gcd(24, 16))

