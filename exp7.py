import heapq
from collections import defaultdict


def best_first_search(graph, start, goal, heuristic):
    # Priority queue to store nodes to be explored (priority, node, path, total_cost)
    open_list = [(heuristic[start], start, [start], 0)]
    # Keep track of visited nodes
    closed_list = set()

    while open_list:
        # Get the node with the lowest heuristic value
        _, current, path, cost = heapq.heappop(open_list)

        # If goal is reached, return the path
        if current == goal:
            return path, cost, closed_list

        # Skip if node has already been visited
        if current in closed_list:
            continue

        # Mark current node as visited
        closed_list.add(current)

        # Explore neighbors
        for neighbor, weight in graph[current]:
            if neighbor not in closed_list:
                # Add neighbor to open list with its heuristic value
                new_path = path + [neighbor]
                new_cost = cost + weight
                heapq.heappush(
                    open_list, (heuristic[neighbor], neighbor, new_path, new_cost)
                )

    # No path found
    return None, 0, closed_list


# Initialize graph using defaultdict
graph = defaultdict(list)
all_nodes = set()

# Read the number of edges
print("Enter the number of edges in the graph:")
num_edges = int(input())

# Read graph edges
print("Enter the edges (node1, node2, weight):")


for i in range(num_edges):
    while True:
        try:
            edge = input(f"Edge {i+1}: ").strip()
            source, destination, weight = edge.split()
            weight = float(weight)

            # Add edge (directed with weight)
            graph[source].append((destination, weight))

            # Add both nodes to all_nodes set
            all_nodes.add(source)
            all_nodes.add(destination)
            break
        except ValueError:
            print("Invalid format. Please use 'node1 node2 weight'.")

# Read heuristic values
print("\nEnter heuristic values for each node:")
heuristic = {}
for node in all_nodes:
    while True:
        try:
            value = float(input(f"Heuristic value for node {node}: "))
            heuristic[node] = value
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get start and goal nodes
start = input("\nEnter start node: ").strip()
goal = input("Enter goal node: ").strip()

# Validate start and goal nodes
if start not in all_nodes:
    print(f"Start node '{start}' not in graph.")
else:
    if goal not in all_nodes:
        print(f"Goal node '{goal}' not in graph.")
    else:
        # Run Best First Search
        path, total_cost, visited = best_first_search(graph, start, goal, heuristic)

        # Display results
        print("\nBest First Search Results:")

        if path:
            print(path)
            print(f"Total cost of path: {total_cost}")
        else:
            print("No path found from start to goal.")
