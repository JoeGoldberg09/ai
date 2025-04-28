from collections import defaultdict
import heapq


def astar(graph, heuristics, start, goal):
    # Priority queue for open nodes: (f_score, node, path)
    open_set = [(heuristics[start], start, [start])]
    # Dictionary to store the cost from start to a node
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0
    # Keep track of visited nodes
    closed_set = set()

    while open_set:
        # Get the node with the lowest f_score
        current_f, current, path = heapq.heappop(open_set)

        # If we've reached the goal, return the path and cost
        if current == goal:
            return path, g_score[goal]

        # Skip if node has already been visited
        if current in closed_set:
            continue

        # Mark current node as visited
        closed_set.add(current)

        # Check all neighbors of the current node
        for neighbor, weight in graph[current]:  # <-- list of (neighbor, weight) tuples
            # Calculate tentative g_score
            tentative_g_score = g_score[current] + weight

            # If we found a better path to the neighbor
            if tentative_g_score < g_score[neighbor] and neighbor not in closed_set:
                # Update our path information
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristics[neighbor]
                new_path = path + [neighbor]

                # Add to open set
                heapq.heappush(open_set, (f_score, neighbor, new_path))

    # If we get here, no path was found
    return None, None


# Create a graph as a defaultdict of list
graph = defaultdict(list)

# Get edges directly from user
print("Enter graph information (directed weighted graph):")
num_edges = int(input("Enter number of edges: "))

# Set to collect all unique nodes
all_nodes = set()

print("Enter edges (source target weight):")
for i in range(num_edges):
    edge_info = input(f"Edge {i+1}: ").split()
    source = edge_info[0]
    target = edge_info[1]
    weight = float(edge_info[2])

    # Add to graph
    graph[source].append((target, weight))  # <-- appending (target, weight) tuple

    # Collect nodes
    all_nodes.add(source)
    all_nodes.add(target)

# Get heuristic values
heuristics = {}
print("\nEnter heuristic values for each node:")
for node in all_nodes:
    heuristic_value = float(input(f"Heuristic for {node}: "))
    heuristics[node] = heuristic_value

# Get start and goal nodes
start_node = input("\nEnter start node: ")
goal_node = input("Enter goal node: ")

# Run A* algorithm
path, cost = astar(graph, heuristics, start_node, goal_node)

# Output results
if path:
    print(f"\nPath found: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print(f"\nNo path found from {start_node} to {goal_node}")
