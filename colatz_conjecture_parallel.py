import concurrent 

def worker(lower, upper):
	for i in range(lower, upper+1):
		assert collatz_check(i, set())
	print('(%d,%d)' % (lower,upper))

def collatz_check(x, visited):
	if x == 1:
		return True
	elif x in visited:
		return False

	visited.add(x)

	if x & 1: #odd number
		return collatz_check(3*x + 1, visited)
	else:
		return collatz_check(x >> 1, visited) #divide by 2

executor = concurrent.futures.ProcessPoolExecutor(max_workers= 17)
with executor:
	for i in range(N // RANGE_SIZE):
		executor.submit(worker, i * RANGE_SIZE + 1, (i_))

