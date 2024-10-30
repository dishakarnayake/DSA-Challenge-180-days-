from collections import deque

# BFS from given source s
def bfs(adj, s):
  
    # Create a queue for BFS
    q = deque()
    
    # Initially mark all the vertices as not visited
    # When we push a vertex into the q, we mark it as 
    # visited
    visited = [False] * len(adj);

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:
      
        # Dequeue a vertex from queue and print it
        curr = q.popleft()
        print(curr, end=" ")

        # Get all adjacent vertices of the dequeued 
        # vertex. If an adjacent has not been visited, 
        # mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# Example usage
if __name__ == "__main__":
  
    # Number of vertices in the graph
    V = 5

    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # Add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    # Perform BFS traversal starting from vertex 0
    print("BFS starting from 0: ")
    bfs(adj, 0)





from collections import deque

# BFS from given source s
def bfs(adj, s, visited):
  
    q = deque() # Create a queue for BFS

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:
        curr = q.popleft() # Dequeue a vertex
        print(curr, end=" ")

        # Get all adjacent vertices of curr
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True # Mark as visited
                q.append(x) # Enqueue it

# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u) # Undirected graph

# Perform BFS for the entire graph
def bfs_disconnected(adj):
    visited = [False] * len(adj) # Not visited

    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj, i, visited)

# Example usage
V = 6 # Number of vertices
adj = [[] for _ in range(V)] # Adjacency list

# Add edges to the graph
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 3, 4)
add_edge(adj, 4, 5)

# Perform BFS traversal for the entire graph
bfs_disconnected(adj)