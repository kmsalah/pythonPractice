class Queue:

	def __init__(self):
		self.queue = []

	def enqueue(self, val):
		self.queue.insert(0, val)

	def dequeue(self):
		if len(self.queue) <=0:
			return "queue empty"
		else:
			return self.queue.pop()

myQ = Queue()

for i in range(10):
	myQ.enqueue(i)
for i in range(11):
	print(myQ.dequeue())