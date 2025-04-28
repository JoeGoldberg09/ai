from collections import defaultdict, deque


# Step 1: Read the graph from user input
graph = defaultdict(list)
n = int(input("Enter the number of edges: "))  # Number of edges
print("Enter the edges (source, destination) one by one:")

for _ in range(n):
    u, v = input().split()  # Read an edge in the form "source destination"
    graph[u].append(v)
    graph[v].append(u)  # Since the graph is undirected



# Step 2: Implement BFS
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()  # Remove the node from the front of the queue
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


start_node = input("Enter the starting node for BFS: ").strip()

# Ensure the start node exists in the graph
if start_node in graph:
    print("BFS Traversal:")
    bfs(graph, start_node)
else:
    print("Start node not found in the graph!")
