#!/user/bin/env python

from minHeap import MinHeap

mHeap = MinHeap()
a = [3,5,6,63,47,2,46,7]
print(a)
mHeap.min_heapify(a)
b = mHeap.heap_sort()
print(b)



maxHeap = MinHeap()
c = [23,123,422,112,42,12,23]
d = [x*-1 for x in c]
maxHeap.min_heapify(d)
e = [x*-1 for x in maxHeap.heap_sort()]
print(e)