from graph_interfaces import IGraph, IVertex
from graph_interfaces import IAlgorithm
from graph_interfaces import AlgorithmResult
from typing import List
import time
from queue import PriorityQueue
from graph_impl import Vertex, Edge
from itertools import count

class greedyBestFirstAlgorithm(IAlgorithm):
    def find_path(self, graph: IGraph, start_vertex_name: str, destination_vertex_name: str) -> AlgorithmResult:
        start_time = time.time()
        vertices_explored = 0
        edges_evaluated = 0

        vertices = {v.get_name(): v for v in graph.get_vertices()}
        start = vertices.get(start_vertex_name)
        goal = vertices.get(destination_vertex_name)
        if not start or not goal:
            return AlgorithmResult(
                textual_directions="Start/destination vertex not found.",
                total_distance=0.0,
                vertices_explored=vertices_explored,
                edges_evaluated=edges_evaluated,
                execution_time=time.time() - start_time,
                path_found=False
            )

        frontier = PriorityQueue()
        counter = count()
        frontier.put((start.straight_line_distance(goal), next(counter), start))
        came_from = {start.get_name(): None}
        total_distance = {start.get_name(): 0.0}
        explored = set()

        while not frontier.empty():
            priority1, tie_break, current = frontier.get()
            if current.get_name() in explored:
                continue
            vertices_explored += 1

            print(f"\nCurrent: {current.get_name()}")
            print("Neighbor distances to Medford:")
            for edge in current.get_edges():
                neighbor = edge.get_destination()
                h_dist = neighbor.straight_line_distance(goal)
                print(f"  {neighbor.get_name()}: {h_dist:.2f} miles")

            if current.get_name() == goal.get_name():
                path = []
                node = current.get_name()
                while node:
                    path.append(node)
                    node = came_from[node]
                path.reverse()
                textual_directions = " -> ".join(path)
                execution_time = time.time() - start_time
                return AlgorithmResult(
                    textual_directions = textual_directions,
                    total_distance = total_distance[goal.get_name()],
                    vertices_explored = vertices_explored,
                    edges_evaluated = edges_evaluated,
                    execution_time = execution_time,
                    path_found = True
                )

            explored.add(current.get_name())
            for edge in current.get_edges():
                edges_evaluated += 1
                neighbor = edge.get_destination()
                if neighbor.get_name() not in explored and neighbor.get_name() not in came_from:
                    frontier.put((neighbor.straight_line_distance(goal), next(counter), neighbor))
                    came_from[neighbor.get_name()] = current.get_name()
                    total_distance[neighbor.get_name()] = total_distance[current.get_name()] + edge.get_weight()

        execution_time = time.time() - start_time
        return AlgorithmResult(
            textual_directions="No path found.",
            total_distance=0.0,
            vertices_explored=vertices_explored,
            edges_evaluated=edges_evaluated,
            execution_time=execution_time,
            path_found=False
        )

    def get_name(self) -> str:
        return "Greedy Best-First Search Algorithm"

class AStarAlgorithm(IAlgorithm):
    def find_path(self, graph: IGraph, start_vertex_name: str, 
                  destination_vertex_name: str) -> AlgorithmResult:
        start_time = time.time()
        vertices_explored = 0
        edges_evaluated = 0

        vertices = {v.get_name(): v for v in graph.get_vertices()}
        start = vertices.get(start_vertex_name)
        goal = vertices.get(destination_vertex_name)
        if not start or not goal:
            return AlgorithmResult(
                textual_directions="Start/destination vertex not found.",
                total_distance=0.0,
                vertices_explored=vertices_explored,
                edges_evaluated=edges_evaluated,
                execution_time=time.time() - start_time,
                path_found=False
            )

        frontier = PriorityQueue()
        frontier.put((start.straight_line_distance(goal), start))
        g_scores = {start.get_name(): 0.0}
        f_scores = {start.get_name(): start.straight_line_distance(goal)}
        came_from = {start.get_name(): None}
        explored = set()

        while not frontier.empty():
            current_f, current = frontier.get()
            vertices_explored += 1

            if current.get_name() == goal.get_name():
                path = []
                node = current.get_name()
                while node:
                    path.append(node)
                    node = came_from[node]
                path.reverse()
                textual_directions = " -> ".join(path)
                execution_time = time.time() - start_time
                return AlgorithmResult(
                    textual_directions=textual_directions,
                    total_distance=g_scores[goal.get_name()],
                    vertices_explored=vertices_explored,
                    edges_evaluated=edges_evaluated,
                    execution_time=execution_time,
                    path_found=True
                )

            explored.add(current.get_name())
            for edge in current.get_edges():
                edges_evaluated += 1
                neighbor = edge.get_destination()
                cost = edge.get_weight()
                tentative_g = g_scores[current.get_name()] + cost
                if neighbor.get_name() not in explored or tentative_g < g_scores.get(neighbor.get_name(), float('inf')):
                    g_scores[neighbor.get_name()] = tentative_g
                    h_neighbor = neighbor.straight_line_distance(goal)
                    f_neighbor = tentative_g + (h_neighbor if h_neighbor is not None else 0)
                    f_scores[neighbor.get_name()] = f_neighbor
                    frontier.put((f_neighbor, neighbor))
                    came_from[neighbor.get_name()] = current.get_name()

        execution_time = time.time() - start_time
        return AlgorithmResult(
            textual_directions="No path found.",
            total_distance=0.0,
            vertices_explored=vertices_explored,
            edges_evaluated=edges_evaluated,
            execution_time=execution_time,
            path_found=False
        )

    def get_name(self) -> str:
        return "A* Search Algorithm"

class DijkstraAlgorithm(IAlgorithm):
    def find_path(self, graph: IGraph, start_vertex_name: str, destination_vertex_name: str) -> AlgorithmResult:
        start_time = time.time()
        vertices_explored = 0
        edges_evaluated = 0

        vertices = {v.get_name(): v for v in graph.get_vertices()}
        start = vertices.get(start_vertex_name)
        goal = vertices.get(destination_vertex_name)
        if not start or not goal:
            return AlgorithmResult(
                textual_directions="Start/destination vertex not found.",
                total_distance=0.0,
                vertices_explored=vertices_explored,
                edges_evaluated=edges_evaluated,
                execution_time=time.time() - start_time,
                path_found=False
            )

        frontier = PriorityQueue()
        counter = count()
        frontier.put((0.0, next(counter), start))
        g_scores = {start.get_name(): 0.0}
        came_from = {start.get_name(): None}
        explored = set()

        while not frontier.empty():
            current_g, priority, current = frontier.get()
            if current.get_name() in explored:
                continue 
            vertices_explored += 1

            if current.get_name() == goal.get_name():
                path = []
                node = current.get_name()
                while node:
                    path.append(node)
                    node = came_from[node]
                path.reverse()
                textual_directions = " -> ".join(path)
                execution_time = time.time() - start_time
                return AlgorithmResult(
                    textual_directions=textual_directions,
                    total_distance=g_scores[goal.get_name()],
                    vertices_explored=vertices_explored,
                    edges_evaluated=edges_evaluated,
                    execution_time=execution_time,
                    path_found=True
                )

            explored.add(current.get_name())
            for edge in current.get_edges():
                edges_evaluated += 1
                neighbor = edge.get_destination()
                cost = edge.get_weight()
                tentative_g = g_scores[current.get_name()] + cost
                if neighbor.get_name() not in explored and tentative_g < g_scores.get(neighbor.get_name(), float('inf')):
                    g_scores[neighbor.get_name()] = tentative_g
                    frontier.put((tentative_g, next(counter), neighbor)) 
                    # next(counter) is the tie-breaker to avoid
                    # the comparison error with two vertices having the same cost score
                    came_from[neighbor.get_name()] = current.get_name()
                    # Records the path taken

        execution_time = time.time() - start_time
        return AlgorithmResult(
            textual_directions="No path found.",
            total_distance=0.0,
            vertices_explored=vertices_explored,
            edges_evaluated=edges_evaluated,
            execution_time=execution_time,
            path_found=False
        )

    def get_name(self) -> str:
        return "Dijkstra's Algorithm"