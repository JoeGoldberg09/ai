import pandas as pd
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
        for neighbor, weight in graph[
            current
        ]:  # Using list of (neighbor, weight) tuples
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


# Read graph from CSV
graph_df = pd.read_csv("exp10_graph.csv")

# Create graph as a defaultdict of lists - each node maps to a list of (neighbor, weight) tuples
graph = defaultdict(list)
for _, row in graph_df.iterrows():
    source = row["node1"]
    target = row["node2"]
    weight = row["weight"]

    # Add edge in both directions since it's undirected
    graph[source].append((target, weight))
    graph[target].append((source, weight))

# Read heuristics from CSV
heuristics_df = pd.read_csv("exp10_heuristics.csv")

# Create heuristics dictionary
heuristics = {}
for _, row in heuristics_df.iterrows():
    heuristics[row["node"]] = row["heuristic_value"]

# Define start and goal nodes
start_node = "A"  # Change as needed
goal_node = "G"  # Change as needed

# Run A* algorithm
path, cost = astar(graph, heuristics, start_node, goal_node)

# Output results
if path:
    print(f"Path found: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print(f"No path found from {start_node} to {goal_node}")
