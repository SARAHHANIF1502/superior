class TreeNode:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.children = []

class Tree:
    def __init__(self):
        self.nodes = []

    def create_node(self, value):
        new_node = TreeNode(value)
        self.nodes.append(new_node)
        return new_node

    def connect_nodes(self, node1, node2):
        node1.children.append(node2)
        node2.children.append(node1)

    def depth_first_search(self, start_node):
        stack = [start_node]
        start_node.visited = True
        while stack:
            current_node = stack.pop()
            print(current_node.value, end="")
            for child in current_node.children:
                if not child.visited:
                    stack.append(child)
                    child.visited = True

tree=Tree()
node_a=tree.create_node('A')
node_b=tree.create_node('B')
node_c=tree.create_node('C')
node_d=tree.create_node('D')
tree.connect_nodes(node_a,node_b)
tree.connect_nodes(node_a,node_c)
tree.connect_nodes(node_b,node_d)
tree.depth_first_search(node_a)
