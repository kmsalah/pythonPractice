class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def longestConsecutive(root):

	longestConsecutive.res = 0
	def longestHelper(node, currLength, expected):
		if node is None:
			return

		if node.data == expected:
			currLength +=1
		else:
			currLength = 1

		longestConsecutive.res = max(longestConsecutive.res, currLength)

		longestHelper(node.left, currLength, node.data + 1)
		longestHelper(node.right, currLength, node.data + 1)



	if root is None:
		return 0 


	longestHelper(root, 0, root.data)

	return longestConsecutive.res



six = Node(6)
six.right = Node(9)
six.right.left = Node(7)
six.right.right = Node(10)
six.right.right.right = Node(11)

print(longestConsecutive(six))
