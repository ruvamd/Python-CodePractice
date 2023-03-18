from asmnt_8 import Graph

def test_shortest_path():
    g = Graph()
    g.add_edge('Queen Anne', 'Capitol Hill', 5)
    g.add_edge('SODO', 'Bellevue', 10)
    g.add_edge('Licton springs','Northgate',2)
    g.add_edge('Ballard','Fremont',7)
    result = g.shortest_path('Queen Anne', 'Bellevue')
    assert result == 15, f"Got {result}, expected 15"
    result = g.shortest_path('Capitol Hill', 'Fremont')
    assert result == 12, f"Got {result}, expected 12"
    result = g.shortest_path('SODO', 'Northgate')
    assert result == 1000000, f"Got {result}, expected 1000000"
    result = g.shortest_path('Ballard', 'Ballard')
    assert result == 0, f"Got {result}, expected 0"

