class Queue:
	def __init__(self):
		self._enq = []
		self._deq = []

	def enqueue(self, x):
		self._enq.append(x)

	def dequeue(self):
		if not self._deq:
			#transfers elements in _enq to _deq
			while self._enq:
				self._deq.append(self._enq.pop())

		if not self._deq:
			raise IndexError('empty queue')
		return self._deq.pop()