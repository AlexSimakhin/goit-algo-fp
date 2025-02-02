"""task5.py"""
import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#222222"):  # Начальный цвет тёмный
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: str(node[1]["label"]) for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color="white")
    plt.show()

def generate_color(step, total):
    intensity = int(255 * (step / total))
    return f"#{intensity:02X}{(intensity // 2):02X}FF"  # Оттенки синего

def bfs(tree_root):
    queue = [tree_root]
    visited = set()
    steps = 0
    total_nodes = count_nodes(tree_root)

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            node.color = generate_color(steps, total_nodes)
            steps += 1
            if node.left and node.left not in visited:
                queue.append(node.left)
            if node.right and node.right not in visited:
                queue.append(node.right)

def dfs(tree_root):
    stack = [tree_root]
    visited = set()
    steps = 0
    total_nodes = count_nodes(tree_root)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            node.color = generate_color(steps, total_nodes)
            steps += 1
            if node.right and node.right not in visited:
                stack.append(node.right)
            if node.left and node.left not in visited:
                stack.append(node.left)

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def array_to_heap_tree(arr):
    if not arr:
        return None
    n = len(arr)
    nodes = [Node(arr[i]) for i in range(n)]
    for i in range(n // 2):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

def main():
    arr = [42, 15, 67, 8, 23, 51, 3, 5, 19]
    root = array_to_heap_tree(arr)

    bfs(root)
    draw_tree(root)

    root = array_to_heap_tree(arr)
    dfs(root)
    draw_tree(root)

if __name__ == "__main__":
    main()
