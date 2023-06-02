import sys

def dijkstra(graph, source):
    # Initialize distances and visited array
    num_nodes = len(graph)
    distances = [sys.maxsize] * num_nodes
    distances[source] = 0
    visited = [False] * num_nodes

    # Find the shortest path for all nodes
    for _ in range(num_nodes):
        # Find the node with the minimum distance from the set of unvisited nodes
        min_dist = sys.maxsize
        min_node = -1
        for v in range(num_nodes):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                min_node = v

        # Mark the selected node as visited
        visited[min_node] = True

        # Update the distances of the adjacent nodes
        for v in range(num_nodes):
            if (not visited[v]) and graph[min_node][v] != 0 and (distances[min_node] + graph[min_node][v] < distances[v]):
                distances[v] = distances[min_node] + graph[min_node][v]

    return distances

# Example graph represented as an adjacency matrix
graph = [
    [0, 2, 0, 4, 0],
    [2, 0, 0, 5, 0],
    [0, 0, 0, 3, 0],
    [4, 5, 3, 0, 1],
    [0, 0, 0, 1, 0]
]

source_node = 0  # Source node is 'A'

distances = dijkstra(graph, source_node)

# Print the shortest distances from the source node
for i, distance in enumerate(distances):
    print(f"Shortest distance from node {source_node} to node {i}: {distance}")
