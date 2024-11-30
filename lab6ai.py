def traverse(graph, start):
    visited = set()
    result = []
    def explore(node, level):
        visited.add(node)
        result.append((node, level))
        for neighbor in graph[node]:
            if neighbor not in visited:
                explore(neighbor, level + 1)
    explore(start, 0)
    return result

connections = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Traversal Order:")
for node, depth in traverse(connections, 'A'):
    print(f"Node: {node}, Depth: {depth}")

from collections import deque

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.adjacents = []

def breadth_first_search(start_node):
    queue = deque([start_node])
    visited = set()
    result = []
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            result.append(current.value)
            queue.extend(neighbor for neighbor in current.adjacents if neighbor not in visited)
    return result

node_a = GraphNode('A')
node_b = GraphNode('B')
node_c = GraphNode('C')
node_d = GraphNode('D')
node_e = GraphNode('E')
node_f = GraphNode('F')

node_a.adjacents = [node_b, node_c]
node_b.adjacents = [node_a, node_d, node_e]
node_c.adjacents = [node_a, node_f]
node_d.adjacents = [node_b]
node_e.adjacents = [node_b, node_f]
node_f.adjacents = [node_c, node_e]

print("BFS Order:", breadth_first_search(node_a))
