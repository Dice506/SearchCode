# Depth-First Search (DFS): This graph traversal algorithm explores as far as possible along each branch before backtracking.
# It's commonly used for problems like maze solving or exploring game trees.

def dfs(graph, start, visited=None):
    # Initialize the visited set if not already done
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(start)

    # Visit all the neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            # Recursively visit each unvisited neighbor
            dfs(graph, neighbor, visited)
    
    # Return the set of visited nodes for reference
    return visited

# Example Graph:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform DFS starting from node 'A'
visited_nodes = dfs(graph, 'A')
print("DFS Traversal:", visited_nodes)

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
# DFS is useful when you want to explore all nodes and paths in a deep, branching structure.
