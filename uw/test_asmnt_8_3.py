#third requirement

import pytest
from asmnt_8_2 import *

def test_shortest_path_exists():
    graph = Graph()
    graph.add_vertex('A', {'B': 1, 'C': 2})
    graph.add_vertex('B', {'A': 1, 'C': 3})
    graph.add_vertex('C', {'A': 2, 'B': 3})
    
    path, distance = graph.ShortestPath('A', 'B')
    
    assert path == ['A', 'B']
    assert distance == 1
    
def test_shortest_path_does_not_exist():
    graph = Graph()
    graph.add_vertex('A', {'B': 1})
    graph.add_vertex('B', {'A': 1})
    graph.add_vertex('C', {})
    
    path, distance = graph.ShortestPath('A', 'C')
    
    assert path == None
    assert distance == None
    
def test_shortest_path_same_start_end():
    graph = Graph()
    graph.add_vertex('A', {'B': 1})
    graph.add_vertex('B', {'A': 1})
    
    path, distance = graph.ShortestPath('A', 'A')
    
    assert path == ['A']
    assert distance == 0
    
def test_shortest_path_reversed():
    graph = Graph()
    graph.add_vertex('A', {'B': 1})
    graph.add_vertex('B', {'A': 1})
    
    path, distance = graph.ShortestPath('B', 'A')
    
    assert path == ['B', 'A']
    assert distance == 1
