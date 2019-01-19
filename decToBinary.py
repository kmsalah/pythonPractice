
def dec_to_binary(n):
	binStr = ''
	while n > 0:
		r = n%2
		binStr += str(r)
		n = n / 2
	return binStr[::-1]

print(dec_to_binary(5))
print(dec_to_binary(9))
print(dec_to_binary(16))
print(dec_to_binary(4))
print(dec_to_binary(19))