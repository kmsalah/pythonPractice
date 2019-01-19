class Stack:
	def __init__(self):
		self.stack = []

	def push(self ,val):
		self.stack.append(val)

	def pop(self):
		if len(self.stack) <= 0:
			return "stack is empty"
		else:
			return self.stack.pop()


myStack = Stack()
for i in range(10, 0, -1):
    myStack.push(i)

for i in range(10):
	print(myStack.pop())



