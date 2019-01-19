def test_collatz_conjecture(n):
	verified_numbers = set()

	for i in range(3, n + 1):
		sequence = set()
		test_i = i
		while test_i >= i:
			if test_i in sequence:
				return False #loop

			sequence.add(test_i)
			if test_i % 2 == 1: #odd number
				if test_i in verified_numbers:
					break
				verified_numbers.add(test_i)
				test_i = 3 * test_i + 1
			else:
				test_i //= 2
	return True


print(test_collatz_conjecture(17))
print(test_collatz_conjecture(100))
print(test_collatz_conjecture(100000000))