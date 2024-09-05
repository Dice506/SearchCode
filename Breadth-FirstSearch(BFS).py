from collections import deque

# Breadth-First Search (BFS): This graph traversal algorithm explores all neighbors at the present depth level 
# before moving on to nodes at the next level. It's used for finding the shortest path in unweighted graphs.

def bfs(graph, start):
    # Initialize the visited set and queue
    visited = set()
    queue = deque([start])

    # Mark the start node as visited
    visited.add(start)

    # While there are nodes to visit
    while queue:
        # Dequeue a node from the front of the queue
        vertex = queue.popleft()

        # Visit all the neighbors of the current node
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # Mark the neighbor as visited and add to the queue
                visited.add(neighbor)
                queue.append(neighbor)

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

# Perform BFS starting from node 'A'
visited_nodes = bfs(graph, 'A')
print("BFS Traversal:", visited_nodes)

# Time Complexity: O(V + E) similar to DFS.
# BFS is great for finding the shortest path or exploring nodes level by level, like in social networks or maps.
