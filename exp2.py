from collections import defaultdict

graph = defaultdict(list)
n = int(input("Enter the number of edges: "))  # Number of edges
print("Enter the edges (source, destination) one by one:")

for _ in range(n):
    u, v = input().split()  # Read an edge in the form "source destination"
    graph[u].append(v)
    graph[v].append(u)  # Since the graph is undirected


# Step 2: Implement non-recursive DFS
def dfs(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            # Add all unvisited neighbors to the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

start_node = input("Enter the starting node for DFS: ").strip()

# Ensure the start node exists in the graph
if start_node in graph:
    print("DFS Traversal (Non-Recursive):")
    dfs(graph, start_node)
else:
    print("Start node not found in the graph!")


