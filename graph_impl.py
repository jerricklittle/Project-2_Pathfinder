from graph_interfaces import IEdge, IGraph, IVertex
from typing import List, Tuple, TypeVar, Optional
import math

# Implementation definitions
# You should implement the bodies of the methods required by the interface protocols.

class Graph(IGraph):
    """Class for Graph implementation using adjacency list representation."""

    def __init__(self) -> None:
        """Constructor for the graph with empty vertex and edge dictionaries.
            Args:
                None
            Returns:
                None
        """
        self.vertices: dict[str, IVertex] = {}
        self.edges: dict[str, IEdge] = {}

    def get_vertices(self) -> List[IVertex]:
        """Get all vertices in the graph.
            Args:
                None
            Returns:
                List of all vertices in the graph.
        """
        return list(self.vertices.values())

    def get_edges(self) -> List[IEdge]:
        """Get all edges in the graph.
            Args:
                None
            Returns:
                List of all edges in the graph.
        """
        return list(self.edges.values())

    def add_vertex(self, vertex: IVertex) -> None:
        """Add a vertex to the graph.
            Args:
                vertex: The vertex to add.
            Returns:
                None
        """
        self.vertices[vertex.get_name()] = vertex

    def remove_vertex(self, vertex_name: str) -> None:
        """Remove a vertex from the graph.
            Args:
                vertex_name: The name of the vertex to remove.
            Returns:
                None
        """
        if vertex_name in self.vertices:
            vertex = self.vertices[vertex_name]
            for edge in list(vertex.get_edges()):
                self.remove_edge(edge.get_name())
            del self.vertices[vertex_name]

    def add_edge(self, edge: IEdge) -> None:
        """Add an edge to the graph.
            Args:
                edge: The edge to add.
            Returns:
                None
        """
        self.edges[edge.get_name()] = edge
        start_vertex = self.vertices.get(edge.get_name().split('->')[0])
        if start_vertex:
            start_vertex.add_edge(edge)

    def remove_edge(self, edge_name: str) -> None:
        """Remove an edge from the graph.
            Args:
                edge_name: The name of the edge to remove.
            Returns:
                None
        """
        if edge_name in self.edges:
            edge = self.edges[edge_name]
            start_vertex_name = edge.get_name().split('->')[0]
            start_vertex = self.vertices.get(start_vertex_name)
            if start_vertex:
                start_vertex.remove_edge(edge_name)
            del self.edges[edge_name]

V = TypeVar('V')

def haversine_distance(lat1, lon1, lat2, lon2) -> float:
    """Calculate the great-circle distance between two points on the Earth."""
    radius = 3959  # Earth's radius in miles
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return radius * c

class Vertex(IVertex):
    """Class for Vertex implementation for the larger Graph Implementation with coordinates."""

    def __init__(self, name: str, latitude: float = None, longitude: float = None) -> None:
        """
        Constructor for the vertex.
            Args:
                name: The name of the vertex.
                latitude: Latitude of the vertex.
                longitude: Longitude of the vertex.
            Returns:
                None
        """
        self._name = name
        self._edges: dict[str, IEdge] = {}
        self._visited: bool = False
        self._data: Optional[V] = None
        self._latitude = latitude
        self._longitude = longitude

    def get_name(self) -> str:
        """Get the name of the vertex.
            Args:
                None
            Returns:
                The name of the vertex.
        """
        return self._name

    def set_name(self, name: str) -> None:
        """Set the name of the vertex.
            Args:
                name: The new name of the vertex.
            Returns:
                None
        """
        self._name = name

    def add_edge(self, edge: IEdge) -> None:
        """Add an edge to the vertex.
            Args:
                edge: The edge to add.
            Returns:
                None
        """
        self._edges[edge.get_name()] = edge

    def remove_edge(self, edge_name: str) -> None:
        """Remove an edge from the vertex.
            Args:
                edge_name: The name of the edge to remove.
            Returns:
                None
        """
        if edge_name in self._edges:
            del self._edges[edge_name]

    def get_edges(self) -> List[IEdge]:
        """Get all edges connected to the vertex.
            Args:
                None
            Returns:
                List of edges connected to the vertex.
        """
        return list(self._edges.values())

    def set_visited(self, visited: bool) -> None:
        """Set the visited status of the vertex.
            Args:
                visited: The visited status to set.
            Returns:
                None
        """
        self._visited = visited

    def is_visited(self) -> bool:
        """Check if the vertex has been visited.
            Args:
                None
            Returns:
                True if the vertex has been visited, False otherwise.
        """
        return self._visited

    def set_coordinates(self, latitude: float, longitude: float) -> None:
        """Set the coordinates for the vertex.
            Args:
                latitude: Latitude of the vertex.
                longitude: Longitude of the vertex.
            Returns:
                None
        """
        self._latitude = latitude
        self._longitude = longitude

    def get_coordinates(self) -> Optional[tuple[float, float]]:
        """Get the coordinates of the vertex.
            Args:
                None
            Returns:
                Tuple of the latitude & longitude if they are
                set, if they are not, returns None.
        """
        if self._latitude is not None and self._longitude is not None:
            return (self._latitude, self._longitude)
        return None

   
    # Replace with Haversine Formula so that it is more accurate for lat/lon.

    def straight_line_distance(self, other: 'Vertex') -> Optional[float]:
        """Calculates the Haversine distance to another vertex in miles.
        Args:
            other: The other vertex to calculate the distance to.
        Returns:
            The Haversine distance to the other vertex if both vertices
            have coordinates, otherwise None.
        """
        if self.get_coordinates() and other.get_coordinates():
            lat1, lon1 = self.get_coordinates()
            lat2, lon2 = other.get_coordinates()
            return haversine_distance(lat1, lon1, lat2, lon2)
        return None
    

class Edge(IEdge):

    """Class for Edge implementation for the larger Graph Implementation."""

    def __init__(self, name: str, destination: IVertex, weight: float = 1.0) -> None:
        """Constructor for the edge.
            Args:
                name: The name of the edge.
                destination: The destination vertex of the edge.
                weight: The weight of the edge (default is 1.0).
            Returns:
                None
        """
        self._name = name
        self._destination = destination
        self._weight = weight

    def get_name(self) -> str:
        """Get the name of the edge.
            Args:
                None
            Returns:
                The name of the edge.
        """
        return self._name

    def set_name(self, name: str) -> None:
        """Set the name of the edge.
            Args:
                name: The new name of the edge.
            Returns:
                None
        """
        self._name = name

    def get_destination(self) -> IVertex:
        """Get the destination vertex of the edge.
            Args:
                None
            Returns:
                The destination vertex of the edge.
        """
        return self._destination

    def get_weight(self) -> float:
        """Get the weight of the edge.
            Args:
                None
            Returns:
                The weight of the edge.
        """
        return self._weight

    def set_weight(self, weight: float) -> None:
        """Set the weight of the edge.
            Args:
                weight: The new weight of the edge.
            Returns:
                None
        """
        self._weight = weight