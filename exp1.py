import pandas as pd
from collections import defaultdict

# Step 1: Read the CSV file
df = pd.read_csv('exp1.csv')  # Make sure the file 'graph.csv' is in the same directory

# Step 2: Build the graph (Adjacency List)
graph = defaultdict(list)

for index, row in df.iterrows():
    u, v = row['source'], row['destination']
    graph[u].append(v)
    graph[v].append(u)  # because the graph is undirected

# Step 3: Implement Recursive DFS
def dfs(node, visited):
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

# Step 4: Run DFS
start_node = input("Enter starting node for DFS: ").strip()
visited = set()

if start_node in graph:
    print("DFS Traversal:")
    dfs(start_node, visited)
else:
    print(f"Start node {start_node} not found in the graph!")


