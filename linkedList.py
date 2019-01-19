class Node:
	def __init__(self, dataval=None):
		self.data = dataval
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def list_print(self):
		current = self.head
		while current is not None:
			print(current.data)
			current = current.next

	def prepend(self, newData):
		newNode = Node(newData)
		newNode.next = self.head
		self.head = newNode

	def append(self, newData):
		current = self.head
		if self.head is None:
			self.head = Node(newData)
			return
		while current.next is not None:
			current = current.next
		current.next = Node(newData)

	def delete(self, key):
		if self.head is None:
			return 

		if self.head.data == key:
			self.head = self.head.next
			return 

		current = self.head
		while current.next is not None:
			if current.next.data == key:
				current.next = current.next.next
				return

			current = current.next



	def delete_dups(self):
		if self.head is None:
			return

		vals = {}
		current = self.head
		vals[current.data] = True

		while current.next is not None:
			if current.next.data in vals:
				current.next = current.next.next
			else:
				vals[current.next.data] = True
				current = current.next
		print(vals)


def isIntersectionLL(list1,list2):
	nodes = {}
	



list = LinkedList()
list.head = Node("mon")
e2 = Node("tues")
e3 = Node("wed")

list.head.next = e2
e2.next = e3

list.prepend("sun")
list.append("thurs")
list.append("thurs")
list.append("thurs")
list.append("thurs")
list.append("thurs")
list.append("thurs")
list.list_print()
print("--------")
list.delete_dups()
list.list_print()





