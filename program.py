from typing import Optional
from graph_interfaces import IGraph, IVertex
from graph_impl import Graph, Vertex, Edge
import csv
from collections import deque
from graph_interfaces import IAlgorithm
from graph_interfaces import AlgorithmResult
from graph_interfaces import IGraph, IVertex
from algorithms import DijkstraAlgorithm, greedyBestFirstAlgorithm, AStarAlgorithm

def read_graph(graph_file_path: str, vertices_file_path: str = "vertices_v1.txt") -> IGraph:  
    """Read the graph and vertex coordinates from the files and 
    return the graph object through populating it.
        Args:
            graph_file_path: Path to the CSV file that has the graph data, 
            in this case, graph_v2.txt.
            vertices_file_path: Path to the CSV file that has the vertex data, 
            in this case, vertices_v1.txt.
        Returns:
            Graph populated with the data from read in from the previously 
            mentioned files.
    """
    graph = Graph()
    vertices = {}
    coords = {}
    with open(vertices_file_path, newline='') as vfile:
        vreader = csv.DictReader(vfile)
        for row in vreader:
            name = row['vertex']
            lat = float(row['latitude'])
            lon = float(row['longitude'])
            coords[name] = (lat, lon)
    
    with open(graph_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            source = row['source']
            destination = row['destination']
            highway = row['highway']
            distance = float(row['distance'])
            # Create source vertex if not exists
            if source not in vertices:
                lat, lon = coords.get(source, (None, None))
                v_source = Vertex(source, lat, lon)
                vertices[source] = v_source
                graph.add_vertex(v_source)
            # Create destination vertex if not exists
            if destination not in vertices:
                lat, lon = coords.get(destination, (None, None))
                v_destination = Vertex(destination, lat, lon)
                vertices[destination] = v_destination
                graph.add_vertex(v_destination)
            edge_name = f"{source}->{destination}"
            edge = Edge(edge_name, vertices[destination], distance)
            graph.add_edge(edge)
    return graph


def main() -> None:
    graph: IGraph = read_graph("graph_v2.txt", "vertices_v1.txt")
    algorithms = {
        "1": DijkstraAlgorithm(),
        "2": greedyBestFirstAlgorithm(),
        "3": AStarAlgorithm()
    }
    algo_names = {
        "1": "Dijkstra's Algorithm",
        "2": "Greedy Best-First Search",
        "3": "A* Algorithm"
    }

    print("Welcome to the Oregon Pathfinder!")
    while True:
        print("\nSelect pathfinding algorithm:")
        print("1. Dijkstra's Algorithm")
        print("2. Greedy Best-First Search")
        print("3. A* Algorithm")
        choice = input("Enter choice (1-3): ").strip()
        if choice not in algorithms:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        start_city = input("\nEnter start city: ").strip()
        dest_city = input("Enter destination city: ").strip()

        print(f"\nRunning {algo_names[choice]}...\n")
        algorithm: IAlgorithm = algorithms[choice]
        result: AlgorithmResult = algorithm.find_path(graph, start_city, dest_city)

        if result.path_found:
            print(f"Path found: {result.textual_directions.replace('->', '→')}")
            print(f"Total distance: {result.total_distance} miles")
        else:
            print("No path found.")
        print(f"Vertices explored: {result.vertices_explored}")
        print(f"Edges evaluated: {result.edges_evaluated}")
        print(f"Execution time: {result.execution_time:.3f} seconds\n")

        again = input("Search another route? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using the Oregon Pathfinder!")
            break

if __name__ == "__main__":
    main()