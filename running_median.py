import heapq

def running_median(sequence):

	#min_heap stores larger half seen so far
	min_heap = []

	#max_heap stores smaller half seen so far
	#values in max_heap are negative for data structure
	max_heap = []
	result = []

	for x in sequence:
		#push onto max_heap, negative of a pop of min_heap, push x onto min_heap
		heapq.heappush(max_heap, -(heapq.heappushpop(min_heap, x)))

		#ensure both heaps have equal number of elements if even num of elements, else
		#minheap has one more

		if len(max_heap) > len(min_heap):
			heapq.heappush(min_heap, -heapq.heappop(max_heap))

		if len(max_heap) == len(min_heap):
			result.append(0.5 * (min_heap[0] + (-max_heap[0])))
		else:
			result.append(min_heap[0])
	return result

print(running_median([1,0,3,5,2,0,1]))