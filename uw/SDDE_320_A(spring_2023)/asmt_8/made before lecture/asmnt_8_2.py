#second requirement

import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def ShortestPath(self, start, end):
        # initialize distances and previous vertices
        distances = {v: float('inf') for v in self.vertices}
        previous_vertices = {v: None for v in self.vertices}

        # set the distance of the starting vertex to 0
        distances[start] = 0

        # create a priority queue and add the starting vertex to it
        pq = [(0, start)]

        while len(pq) > 0:
            # pop the vertex with the smallest distance from the priority queue
            current_distance, current_vertex = heapq.heappop(pq)

            # if we've reached the end vertex, we can terminate the search and return the path
            if current_vertex == end:
                path = []
                while current_vertex is not None:
                    path.append(current_vertex)
                    current_vertex = previous_vertices[current_vertex]
                path.reverse()
                return path, distances[end]

            # check the distances to the neighbors of the current vertex
            for neighbor in self.vertices[current_vertex]:
                if neighbor not in distances:
                    continue

                # calculate the tentative distance to the neighbor
                tentative_distance = current_distance + self.vertices[current_vertex][neighbor]

                # if the tentative distance is smaller than the current distance, update the distances
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    previous_vertices[neighbor] = current_vertex

                    # add the neighbor to the priority queue
                    heapq.heappush(pq, (tentative_distance, neighbor))

        # if we get here, there's no path from start to end
        return None

graph = Graph()
graph.add_vertex('Queen Anne', {'Capitol Hill': 5})
graph.add_vertex('Capitol Hill', {'Queen Anne': 5, 'Downtown': 3})
graph.add_vertex('Downtown', {'Capitol Hill': 3, 'SODO': 4})
graph.add_vertex('SODO', {'Downtown': 4, 'Bellevue': 10})
graph.add_vertex('Bellevue', {'SODO': 10})

path, distance = graph.ShortestPath('Queen Anne', 'Bellevue')
print('Shortest path:', path)
print('Shortest distance:', distance)
