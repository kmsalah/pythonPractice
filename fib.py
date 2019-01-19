def fib(n):
	if n == 0 or n == 1:
		return n
	return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(4))
print(fib(30))


#caching intermediate results
def memFib(n , cache = {}):
	if n <= 1:
		return n
	elif n not in cache:
		cache[n] = memFib(n-1) + memFib(n-2)
	return cache[n]

print(memFib(30))


#minimizing cache space, iterativaly fills in the cache in a bottom up fashion whcih allows it to reuse cache storage to reduce space complexity
def littleFib(n):
	if n <= 1:
		return n

	f_minus_2 = 0
	f_minus_1 = 1

	for _ in range(1, n):
		f = f_minus_2 + f_minus_1
		f_minus_2 = f_minus_1
		f_minus_1 = f
	return f_minus_1