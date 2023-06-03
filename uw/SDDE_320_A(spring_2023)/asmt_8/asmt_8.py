'''
BFS of a Graph
Complete the function bfsOfGraph(V, AdjacencyList) which takes the 
integer V denoting the number of vertices and an adjacency list as 
input parameters and returns a list containing the BFS traversal of 
the graph starting from the 0th vertex from left to right.

DFS of a Graph
Complete the function dfsOfGraph(V, AdjacencyList) which takes the 
integer V denoting the number of vertices and an adjacency list as 
input parameters and returns a list containing the DFS traversal of 
the graph starting from the 0th vertex from left to right.
'''
from collections import deque

def bfsOfGraph(V, AdjacencyList):
    visited = [False] * V  # Mark all vertices as not visited
    result = []  # To store the BFS traversal
    
    # Create a queue for BFS
    queue = deque()
    queue.append(0)  # Start from vertex 0
    visited[0] = True  # Mark vertex 0 as visited
    
    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        result.append(vertex)  # Add the vertex to the result
        
        # Visit all adjacent vertices of the current vertex
        for adjacent in AdjacencyList[vertex]:
            if not visited[adjacent]:
                queue.append(adjacent)  # Enqueue the adjacent vertex
                visited[adjacent] = True  # Mark the adjacent vertex as visited
    
    return result

def dfsOfGraph(V, AdjacencyList):
    visited = [False] * V  # Mark all vertices as not visited
    result = []  # To store the DFS traversal
    
    def dfs(vertex):
        visited[vertex] = True  # Mark the current vertex as visited
        result.append(vertex)  # Add the vertex to the result
        
        # Visit all adjacent vertices of the current vertex
        for adjacent in AdjacencyList[vertex]:
            if not visited[adjacent]:
                dfs(adjacent)  # Recursive call to visit the adjacent vertex
    
    dfs(0)  # Start DFS traversal from vertex 0
    return result

'''
    0
   / \
  1   2
 / \   \
3   4   5
'''

V = 6  # Number of vertices
AdjacencyList = [
    [1, 2],     # Adjacent vertices of vertex 0
    [0, 3, 4],  # Adjacent vertices of vertex 1
    [0, 5],     # Adjacent vertices of vertex 2
    [1],        # Adjacent vertices of vertex 3
    [1],        # Adjacent vertices of vertex 4
    [2]         # Adjacent vertices of vertex 5
]

# Function calls
bfs_result = bfsOfGraph(V, AdjacencyList)
dfs_result = dfsOfGraph(V, AdjacencyList)

# Output
print("BFS Traversal:", bfs_result)
print("DFS Traversal:", dfs_result)
