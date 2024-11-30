class Node:
    def __init__(self, row, col, cost, parent):
        self.row = row
        self.col = col
        self.cost = cost
        self.parent = parent

def heuristic(node, goal):
    return abs(node.row - goal[0]) + abs(node.col - goal[1])

def astar_algorithm(start, goal, grid):
    open_list = []
    closed_set = set()
    start_node = Node(start[0], start[1], 0, None)
    open_list.append(start_node)

    while open_list:
        current = min(open_list, key=lambda n: n.cost + heuristic(n, goal))
        open_list.remove(current)
        closed_set.add((current.row, current.col))
        if (current.row, current.col) == goal:
            path = []
            while current:
                path.append((current.row, current.col))
                current = current.parent
            return path[::-1]

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = current.row + dr, current.col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != 1:
                new_node = Node(new_row, new_col, current.cost + 1, current)
                if (new_row, new_col) not in closed_set:
                    open_list.append(new_node)

    return None

grid = [
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

start_point = (0, 0)
goal_point = (4, 5)
path = astar_algorithm(start_point, goal_point, grid)
if path:
    print("A* Path:", path)
else:
    print("No path found")
