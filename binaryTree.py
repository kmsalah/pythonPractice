class BinaryTreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


	def inOrderTraversal(self, binaryTreeNode):
		res = []
		if binaryTreeNode:
			res = self.inOrderTraversal(binaryTreeNode.left)
			res.append(binaryTreeNode.data)
			res = res + self.inOrderTraversal(binaryTreeNode.right)
		return res

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

	int pathsFromRoot = countPathsWithSumFromNode(root, targetSum, 0)

	int pathsOnLeft = pathsWithSum(root.left, targetSum)
	int pathsOnRight = pathsWithSum(root.right, targetSum)

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

root = BinaryTreeNode(10)
root.left = BinaryTreeNode(5)
root.left.left = BinaryTreeNode(3)
root.left.left.left = BinaryTreeNode(3)
root.left.left.right = BinaryTreeNode(-2)



















