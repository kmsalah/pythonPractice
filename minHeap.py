#!/user/bin/env python

class MinHeap:
	def __init__(self):
		self.list = [0]
		self.size = 0

	def bubble_up(self, size):
		while size // 2 > 0:
			if self.list[size] < self.list[size//2]:
				self.list[size], self.list[size//2] = self.list[size//2],self.list[size]
			size = size//2

	def insert(self, k):
		self.list.append(k)
		self.size += 1
		self.bubble_up(self.size)

	def min_child(self, i):
		if (i * 2 + 1) > self.size:
			return (i * 2)
		else:
			if self.list[i * 2] < self.list[(i * 2) + 1]:
				return (i * 2)
			else:
				return ((i * 2) +1)

	def bubble_down(self, i):
		while i * 2 <= self.size:
			mc = self.min_child(i)
			if self.list[i] > self.list[mc]:
				self.list[i],self.list[mc] = self.list[mc], self.list[i]
			i = mc

	def pop(self):
		ret_val = self.list[1]
		self.list[1] = self.list[self.size]
		self.size -= 1
		self.list.pop()
		self.bubble_down(1)
		return ret_val

	def min_heapify(self, aList):
		i = len(aList) // 2
		self.size = len(aList)
		self.list = [0] + aList[:]
		while i > 0:
			self.bubble_down(i)
			i -= 1

	def heap_sort(self):
		i = self.size
		sortedVals = []
		while i > 0:
			sortedVals.append(self.pop())
			i-=1
		return sortedVals

