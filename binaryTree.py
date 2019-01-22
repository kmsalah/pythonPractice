class BinaryTreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


	def preOrderTraversal(self, root):
		def preHelper(node):
			if node:
				res.append(node.data)
				preHelper(node.left)
				preHelper(node.right)
		res = []
		preHelper(root)
		print(res)
'''

	def iterativeInOrderTraversaL(self, root):
		res = []
		stack = [root]
		while stack:
			if stack[-1].left and stack[-1].left not in res :
				stack.append(stack[-1].left)
				continue
			else:
				node = stack.pop()
				res.append(node)
				if node.right:
					stack.append(node.right)
		return res
'''

	def inOrderTraversal(self, root):
		def inhelper(node):
			if node:
				inhelper(node.left)
				res.append(node.data)
				inhelper(node.right)
		res = []
		inhelper(root)
		print(res)

	def postOrderTraversal(self, root):
		def posthelper(node):
			if node:
				posthelper(node.left)
				posthelper(node.right)
				res.append(node.data)
		res = []
		posthelper(root)
		print(res)

	#bfs
	def levelOrderTraversal(self, root):
		if root is None:
			return

		res = []
		queue = []
		queue.append(root)

		while queue:
			res.append(queue[0].data)
			node = queue.pop(0)

			if node.left is not None:
				queue.append(node.left)

			if node.right is not None:
				queue.append(node.right)

		print(res)






def isSymmetric(root):
	if root:
		return isMirror(root, root)
def isMirror(root1, root2):
	#both trees are empty, then they mirror images
	if root1 is None and root2 is None:
		return True

	"""
         keys must be same, left subtree of root 1 must be same as right subtree of root 2,
         right subtree of root 1 must be same as left subtree of root 2
	"""
	if root1 is not None and root2 is not None:
		if root1.data == root2.data:
			return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

	return False


def pathsWithSum(root, targetSum):
	if root is None:
		return 0

	pathsFromRoot = countPathsWithSumFromNode(root, targetSum, 0)

	pathsOnLeft = pathsWithSum(root.left, targetSum)
	pathsOnRight = pathsWithSum(root.right, targetSum)

	return pathsFromRoot + pathsOnLeft + pathsOnRight



def countPathsWithSumFromNode(node, targetSum, currentSum):
	if node is None:
		return 0

	currentSum += node.data

	totalPaths = 0

	if currentSum == targetSum:
		totalPaths += 1


	totalPaths += countPathsWithSumFromNode(node.left, targetSum, currentSum)
	totalPaths += countPathsWithSumFromNode(node.right, targetSum, currentSum)

	return totalPaths




'''
root = BinaryTreeNode(314)

root.left = BinaryTreeNode(6)
root.left.right = BinaryTreeNode(561)
root.left.right.right = BinaryTreeNode(3)


root.right = BinaryTreeNode(6)
root.right.left = BinaryTreeNode(561)
print(isSymmetric(root))

'''

'''
root = BinaryTreeNode(10)
root.left = BinaryTreeNode(5)
root.left.left = BinaryTreeNode(3)
root.left.left.left = BinaryTreeNode(3)
root.left.left.right = BinaryTreeNode(-2)


root.preOrderTraversal(root)
root.inOrderTraversal(root)
root.postOrderTraversal(root)

'''


root = BinaryTreeNode(10)
root.left = BinaryTreeNode(7)
root.left.left = BinaryTreeNode(8)
root.left.right = BinaryTreeNode(2)
root.left.right.right = BinaryTreeNode(4)
root.left.right.right.left = BinaryTreeNode(20)
root.right = BinaryTreeNode(6)
root.right.left = BinaryTreeNode(69)
root.right.left.left = BinaryTreeNode(5)

root.preOrderTraversal(root)
root.inOrderTraversal(root)
#root.iterativeInOrderTraversaL(root)
root.postOrderTraversal(root)

root.levelOrderTraversal(root)














