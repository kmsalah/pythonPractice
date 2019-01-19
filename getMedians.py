class maxHeapComp(float):
	def __lt__(self, other):
			return not float.__le__(self, other)
		def __le__(self, other):
			return not float.__lt__(self, other)
		def __gt__(self, other):
			return not float.__ge__(self, other)
		def __ge__(self, other):
			return not float.__gt__(self, other)


def addNumber(num ,lowers, highers):
	if len(lowers) == 0 or num < lowers[-1]:
		heapq.heappush(lowers, maxHeapComp(num))
	else:
		heapq.heappush(highers, num)

def rebalance(lowers, highers):
	bigHeap = len(lowers) > len(highers) ? lowers : highers
	smallHeap = len(lowers) > len(highers) ? highers : lowers

	if len(bigHeap) - len(smallHeap) >= 2:
		popped = heapq.heappop(highers)
		heapq.heappush(lowers, heap)

def getMedian(lowers, highers):
	bigHeap = len(lowers) > len(highers) ? lowers : highers
	smallHeap = len(lowers) > len(highers) ? highers : lowers

	if len(bigHeap) == len(smallHeap):
		return (heapq.heappop(highers) + heapq.heappop(lowers)) / 2


def getMedians(arr):
	lowers = [] #max heap
	highers = [] #min heapp

	medians = list(len(arr))

	for i in range(len(arr)):
		num = arr[i]
		addNumber(num,lowers,highers)
		rebalance(lowers, highers)
		medians[i] = getMedian(lowers, highers)

	return medians


