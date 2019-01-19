class BSTNode:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right 

def search_bst(treeNode, key):
	if treeNode is None or treeNode.data == key:
		return treeNode

	if treeNode.val < key:
		return search_bst(treeNode.right, key)

	return search_bst(treeNode.left, key)

def find_LCA(root, s, b):
	 while root.data < s.data or tree.data > b.data:
	 	while root.data < s.data
	 		root = root.right
	 	while root.data > b.data
	 		root = root.left
	 return root 