import random
import operator

def findKthLargest(A, k):
	def findKth():
		def parition_around_pivot(l, r, p_idx):
			pivot_val = A[p_idx]
			new_pivot_idx = l 
			A[p_idx], A[r] = A[r], A[p_idx]

			for i in range(l, r):
				if A[i] > pivot_val:
					A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
					new_pivot_idx += 1

			A[r], A[new_pivot_idx] = A[new_pivot_idx], A[r]
			return new_pivot_idx


		left = 0
		right = len(A) -1

		while left <= right:
			pivot_idx = random.randint(left, right)
			new_pivot_idx = parition_around_pivot(left, right, pivot_idx)

			if new_pivot_idx == k-1:
				return A[new_pivot_idx]
			elif new_pivot_idx > k-1:
				right = new_pivot_idx - 1
			else:
				left = new_pivot_idx + 1

	return findKth()



print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))