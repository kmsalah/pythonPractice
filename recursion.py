def permutations(A):
	def directed_permutations(i):
		if i == len(A) - 1:
			result.append(A.copy())
			return

		for j in range(i, len(len(A))):
			A[i], A[j] = A[j], A[i]
			#generate all perms for A[i + 1]
			direted_permutations(i+1)
			A[i], A[j] = A[j], A[i]

	result = []
	directed_permutations(0)
	return result


def fibonacci(i):
	if i == 0: 
		return 0
	if i == 1:
		return 1
	return fibonacci(i-1) + fibonacci(i-2)


def mFib(i):
	return mFib(i, list(i+1))
def mFib(i, memo):
	if i ==0 or i==1:
		return 1
	if memo[i] is None:
		memo[i] == fib(i-1, memo) + fib(i-2, memo)
	return memo[i]