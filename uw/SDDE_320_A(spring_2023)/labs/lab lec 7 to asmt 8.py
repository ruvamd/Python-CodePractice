#lab from lesson 7

def create_graph_1():
    graph = {'a': ['b', 'c'], 
             'b': ['d', 'e'], 
             'c': ['f', 'g'], 
             'd': ['h', 'i'],
             'e': [],
             'f': [],
             'g': [],
             'h': [],
             'i': []}
    return graph

def create_graph_2():
    graph = {'a': ['b'], 
             'b': ['c'], 
             'c': ['d', 'c1'], 
             'd': ['d1'], 
             'd1': ['d2'], 
             'c1': ['c2']}
    return graph

#DFS

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    if start in graph:
        for next_vertex in graph[start]:
            if next_vertex not in visited:
                dfs(graph, next_vertex, visited)

#BFS

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        print(vertex)
        if vertex in graph:
            for next_vertex in graph[vertex]:
                if next_vertex not in visited:
                    visited.add(next_vertex)
                    queue.append(next_vertex)

#output

graph = create_graph_1()
dfs(graph, 'a')
bfs(graph, 'a')

graph = create_graph_2()
dfs(graph, 'a')
bfs(graph, 'a')

'''
a
b
d
h
i
e
c
f
g
a
b
c
d
e
f
g
h
i
a
b
c
d
d1
d2
c1
c2
a
b
c
d
c1
d1
c2
d2
'''