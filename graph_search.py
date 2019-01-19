from collections import defaultdict 

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFS_helper(self, v, visited):
		visited[v] = True
		print v

		for i in self.graph[v]:
			if visited[i] == False:
				self.DFS_helper(i, visited)

	def DFS(self, v):
		visited = [False] * (len(self.graph))

		self.DFS_helper(v, visited)

	def BFS(self, s):
		visited = [False] * (len(self.graph))

		queue = []

		#enqueue node and mark as visited
		queue.append(s)
		visited[s] = True

		while queue:

			s = queue.pop(0)
			print(s)
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True




g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print "Following is DFS from (starting from vertex 2)"
g.DFS(2) 

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 


