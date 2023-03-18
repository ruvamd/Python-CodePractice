# Define graph
graph = {'Queen Anne': {'Capitol Hill': 5},
         'Capitol Hill': {'Queen Anne': 5, 'Fremont': 6},
         'Fremont': {'Capitol Hill': 6, 'Ballard': 3},
         'Ballard': {'Fremont': 3},
         'SODO': {'Bellevue': 10},
         'Bellevue': {'SODO': 10},
         'Licton Springs': {'Northgate': 2},
         'Northgate': {'Licton Springs': 2}}

# Define function to find shortest path using Dijkstra's algorithm
def ShortestPath(graph, start, end):
    # Create dictionary to store shortest distance to each vertex from start
    shortest_distance = {}
    # Create dictionary to store the previous vertex in the shortest path
    previous_vertex = {}
    # Create list to store visited vertices
    visited = []
    # Create list to store unvisited vertices
    unvisited = []
    # Set the starting vertex's shortest distance to 0
    shortest_distance[start] = 0
    # Add the starting vertex to the unvisited list
    unvisited.append(start)
    # Loop until all vertices have been visited
    while unvisited:
        # Sort the unvisited vertices by their shortest distance from start
        unvisited.sort(key=lambda vertex: shortest_distance.get(vertex, float('inf')))
        # Pop the vertex with the shortest distance from the unvisited list
        current_vertex = unvisited.pop(0)
        # Add the current vertex to the visited list
        visited.append(current_vertex)
        # If we have reached the end vertex, we are done
        if current_vertex == end:
            # Create list to store the shortest path
            path = []
            # Set the distance to the end vertex
            distance = shortest_distance[end]
            # Loop backwards through the previous vertices to find the shortest path
            while current_vertex in previous_vertex:
                path.insert(0, current_vertex)
                current_vertex = previous_vertex[current_vertex]
            path.insert(0, start)
            # Return the shortest path and distance
            return path, distance
        # Loop through the neighbors of the current vertex
        for neighbor in graph[current_vertex]:
            # If the neighbor has not been visited, add it to the unvisited list
            if neighbor not in visited:
                # Calculate the distance from start to the neighbor through the current vertex
                distance = shortest_distance[current_vertex] + graph[current_vertex][neighbor]
                # If the distance is shorter than the neighbor's current shortest distance, update it
                if distance < shortest_distance.get(neighbor, float('inf')):
                    shortest_distance[neighbor] = distance
                    previous_vertex[neighbor] = current_vertex
                    if neighbor not in unvisited:
                        unvisited.append(neighbor)
    # If we have visited all vertices and have not found a path to the end vertex, return None
    return None

# Test the function with some examples
path, distance = ShortestPath(graph, 'Queen Anne', 'Capitol Hill')
print("Shortest path from Queen Anne to Capitol Hill:", path)
print("Shortest distance from Queen Anne to Capitol Hill:", distance)

path, distance = ShortestPath(graph, 'Licton Springs', 'Northgate')
print("Shortest path from Licton Springs to Northgate:", path)
print("Shortest distance from Licton Springs to Northgate:", distance)

path, distance = ShortestPath(graph, 'SODO', 'Bellevue')
print("Shortest path from SODO to Bellevue:", path)
print("Shortest distance from SODO to Bellevue:", distance)
