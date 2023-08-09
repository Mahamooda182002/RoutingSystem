import networkx as nx
import requests

# Example map data (simplified)
map_data = {
    "nodes": {
        "A": {"lat": 37.7749, "lon": -122.4194},
        "B": {"lat": 37.3382, "lon": -121.8863},
        "C": {"lat": 34.0522, "lon": -118.2437},
        # Add more nodes...
    },
    "edges": [
        ("A", "B"),
        ("B", "C"),
        # Add more edges...
    ]
}

# Create a graph using NetworkX and add nodes and edges
G = nx.Graph()
for node, data in map_data["nodes"].items():
    G.add_node(node, pos=(data["lat"], data["lon"]))
for edge in map_data["edges"]:
    G.add_edge(edge[0], edge[1])

# Dijkstra's shortest path algorithm
def shortest_path(source, destination):
    shortest_path = nx.shortest_path(G, source, destination)
    return shortest_path

# Example usage
source = "A"
destination = "C"
optimal_route = shortest_path(source, destination)
print("Optimal route:", optimal_route)
