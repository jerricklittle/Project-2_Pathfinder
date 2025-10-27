# Project-2_Pathfinder
## Pathfinding Algorithm Implementation (Greedy BFS, Dijkstra, A*)
## Names: Jerrick Little and Aj Tennathur
## Course: CS 351 Analysis of Algorithms


## How to Compile/Run the Program

#### Setup 
1. Ensure all project files are in the same directory: 
- `program.py` (main entry point) 
- `algorithms.py` (pathfinding algorithms) 
- `graph.txt` (cities with distances)
- `graph_interfaces.py` (interface definitions for graph components)
- `vertices_v1.txt` (cities with lat and long values)
- `graph_impl.py` (Graph, Vertex, and Edge class implementations)


## Empirical Analysis

PORTLAND TO MEDFORD

Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 2

Enter start city: Portland
Enter destination city: Medford

Running Greedy Best-First Search...

Path found: Portland → Newport → Florence → Coos_Bay → Roseburg → Medford
Total distance: 397.0 miles
Vertices explored: 6
Edges evaluated: 15
Execution time: 0.002 seconds

Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 1

Enter start city: Portland
Enter destination city: Medford

Running Dijkstra's Algorithm...

Path found: Portland → Salem → Eugene → Roseburg → Medford
Total distance: 268.0 miles
Vertices explored: 19
Edges evaluated: 48
Execution time: 0.001 seconds

Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 3

Enter start city: Portland
Enter destination city: Medford

Running A* Algorithm...

Path found: Portland → Salem → Eugene → Roseburg → Medford
Total distance: 268.0 miles
Vertices explored: 6
Edges evaluated: 18
Execution time: 0.001 seconds


PORTLAND TO ASHLAND:

Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 2

Enter start city: Portland
Enter destination city: Ashland

Running Greedy Best-First Search...

Path found: Portland → Newport → Florence → Coos_Bay → Roseburg → Medford → Ashland
Total distance: 412.0 miles
Vertices explored: 7
Edges evaluated: 18
Execution time: 0.001 seconds

Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 1

Enter start city: Portland
Enter destination city: Ashland

Running Dijkstra's Algorithm...

Path found: Portland → Salem → Eugene → Roseburg → Medford → Ashland
Total distance: 283.0 miles
Vertices explored: 20
Edges evaluated: 51
Execution time: 0.001 seconds

Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 3

Enter start city: Portland
Enter destination city: Ashland

Running A* Algorithm...

Path found: Portland → Salem → Eugene → Crater_Lake → Medford → Ashland
Total distance: 311.0 miles
Vertices explored: 10
Edges evaluated: 30
Execution time: 0.001 seconds

PORTLAND TO EUGENE

Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 1

Enter start city: portland
Enter destination city: Eugene

Running Dijkstra's Algorithm...

Path found: portland → salem → eugene
Total distance: 111.0 miles
Vertices explored: 6
Edges evaluated: 11
Execution time: 0.000 seconds


Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 2

Enter start city: Portland
Enter destination city: Eugene

Running Greedy Best-First Search...

Path found: Portland → Salem → Eugene
Total distance: 111.0 miles
Vertices explored: 3
Edges evaluated: 7
Execution time: 0.000 seconds


Select pathfinding algorithm:
1. Dijkstra's Algorithm
2. Greedy Best-First Search
3. A* Algorithm
Enter choice (1-3): 3

Enter start city: portland
Enter destination city: eugene

Running A* Algorithm...

Path found: portland → salem → eugene
Total distance: 111.0 miles
Vertices explored: 6
Edges evaluated: 11
Execution time: 0.000 seconds

REFLECTION:
- All three algorithms found the optimal path for Portland to Eugene. Dijkstra found the optimal path for Portland to Ashland. Finally, Dijkstra and A star found the optimal path for Portland to Medford.
- On average, Dijkstra performed best in regards to finding optimal paths. In the case of Portland to Eugene, all three algorithms performed similarly, getting the same optimal path. 
Vertices Explored:
Portland to Medford
- GBFS: 6
- Dijkstra: 48
- A*: 6
Portland to Ashland: 
- GBFS: 7
- Dijkstra: 20
- A*: 10
Portland to Eugene:
- GBFS: 6
- Dijkstra: 3
- A*: 6


## Algorithm Use Case Analysis and Comparison

### When is Dijkstra's performance best?
Dijkstra excels in situations like:
- Applications like emergency routing, fuel-efficient navigation, or delivery optimization where finding the guaranteed shortest path is more important than speed.
- When there are multiple paths with similar distances, Dijkstra guarantees finding the absolute shortest path by exploring all possibilities systematically.
### When Greedy BFS finds suboptimal paths
Greedy BFS struggles in situations such as:
- When the straight-line heuristic points toward the goal but natural barriers (like mountain ranges) force longer detours.
- When major highways don't run in a straight line toward the destination.
### When A* showcases its strengths
A* demonstrates superiority in situations like:
- When the graph is large enough that Dijkstra's explores too many unnecessary nodes, but structured enough that the heuristic provides good guidance.
- In a large graph, A* maintains a frontier of promising nodes rather than exhaustively exploring in all directions like Dijkstra.
### Real World Applications
- Dijkstra: Small to medium sized graph, no reliable heuristic is available, and absolute optimality is required (emergency services).
- Greedy BFS: Limited memory and speed is more important than optimality
- A*: Optimality and efficiency are significant, large graphs (cities), and a good heuristic is available.
## Runtime Complexity Analysis

### Time Complexity
Dijkstra
- Time complexity is O((E+V)logV) because we’re using a priority queue
- V = vertices (cities)
- E = Edges (connecting road segments)
- WORST CASE: Must explore every vertex and edge in the graph

Greedy BFS
- Best case time complexity is O(E) (linear) but worst case complexity is O(b^m) (exponential)
- Highly dependent on heuristic quality - can be very fast or very slow
- BEST CASE: Directly follows heuristic to goal with minimal exploration 
- WORST CASE: May explore most of the graph if heuristic is misleading
A*
- Time complexity is the same as dijkstra (O((E+V)logV)) for the same reason as Dijkstra
- Dijkstra only uses g(n) (actual distance) but this added heuristic check of h(n) doesn’t slow down the algorithm rather improves the constant factor
- Performance depends heavily on heuristic quality
### Space Complexity
Dijkstra
- O(V) because you’re storing all of the priority queue, g scores, previous and explored vertices. All of these individually require O(V) storage which is maintained as a whole

Greedy BFS
- O(V) due to the need to store the priority queue, vertices explored, and path which all are O(V).
- Typically stores less V when running compared to A* or Dijkstra because of the focused search using heuristics.

A*
- O(V) because you’re storing the priority queue, g scores, f scores, previous and explored vertices. All of these individually require O(V) storage which is maintained as a whole
### Performance on Oregon Map
- All three algorithms are VERY efficient! All complete in <10ms
- Dijkstra will explore most or all of the 22 vertices
- Greedy BFS could also explore all 22 but, realistically with a good heuristic around ____ vertices
- A* will explore more than greedy but less than Dijkstra due to using a heuristic and g score. Explores about 6-11 vertices
### Performance on Large Scale map (US Highway System)
Dijkstra
- Dijkstra would have to explore most or all cities in the nation. Including those far from the goal.
- Example: Portland to Charlotte might explore cities in California or Arizona before finding optimal path
Greedy
- Should be the fastest algorithm but will likely find suboptimal results for cross country routes
- Mountains or water make the heuristic less reliable.
A*
- Provides optimal solution with less exploration than Dijkstra
- With a good heuristic, performance excels in large scales
### Trade Offs
Dijkstra's: 100% optimal, but slower than A* on large maps
Greedy Best-First: Fastest algorithm, but longer, suboptimal paths
A*: Provides the best of both worlds; Dijkstra's guaranteed shortest path with Greedy's focused search speed
## Heuristic Discussion
### Why is the haversine function admissible for A*?
- Haversine distance is admissible because it never overestimates the actual driving distance. It calculates straight-line distance.
- Roads must follow curves, terrain, and infrastructure.They cannot be shorter than the straight line between two points.
- A* will be guaranteed optimal because the heuristic will always underestimate or equal true cost
### What happens when heuristic underestimates heavily with Greedy BFS?
- Greedy BFS losing direction and starts to perform poorly
- Explores unnecessary nodes in wrong direction
- Becomes slower due to exploration of unnecessary nodes
### Could we design a better heuristic function?
- No, it's basically optimal. Admissible, accurate, fast, and simple
- Trying to improve it seems unnecessary due to the lack of need for improvement 
