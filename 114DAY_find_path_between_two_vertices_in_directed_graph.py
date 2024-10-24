# program to check if there is exist a path between two vertices
# of a graph

from collections import defaultdict

#This class represents a directed graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
	
	# Use BFS to check path between s and d
	def isReachable(self, s, d):
		# Mark all the vertices as not visited
		visited =[False]*(self.V)

		# Create a queue for BFS
		queue=[]

		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			#Dequeue a vertex from queue 
			n = queue.pop(0)
			
			# If this adjacent node is the destination node,
			# then return true
			if n == d:
				return True

			# Else, continue to do BFS
			for i in self.graph[n]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True
		# If BFS is complete without visited d
		return False

# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

u =1; v = 3

if g.isReachable(u, v):
	print("There is a path from %d to %d" % (u,v))
else :
	print("There is no path from %d to %d" % (u,v))

u = 3; v = 1
if g.isReachable(u, v) :
	print("There is a path from %d to %d" % (u,v))
else :
	print("There is no path from %d to %d" % (u,v))




















from typing import List, Tuple

def dfs(start: int, end: int, visited: List[bool], V: int) -> bool:
	if start == end:
		return True
	visited[start] = True
	for x in adj[start]:
		if not visited[x]:
			if dfs(x, end, visited, V):
				return True
	return False

if __name__ == '__main__':
	V = 4
	members = [2, 5, 7, 9]

	E = 4
	connections = [ (2, 9), (7, 2), (7, 9), (9, 5) ]

	member_to_index = {member: i for i, member in enumerate(members)}

	adj = [[] for _ in range(V)]
	for a, b in connections:
		a = member_to_index[a]
		b = member_to_index[b]
		adj[a].append(b)

	sender = member_to_index[7]
	receiver = member_to_index[9]

	visited = [False] * V
	if dfs(sender, receiver, visited, V):
		print("1")
	else:
		print("0")
