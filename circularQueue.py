class Queue:
	SCALE_FACTOR = 2

	def __init__(self, capacity):
		self._entries = [None] * capacity
		self._head = self._tail = self._num_queue_elems = 0
	
	def enqueue(self, x):
		if self._num_queue_elems == len(self._entries): #needs to be resized
			self._entries = (self._entries[self._head:] + self._entries[:self._head])

Queue(5)