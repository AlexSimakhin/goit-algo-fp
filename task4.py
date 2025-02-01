"""task4.py"""
import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас для представлення вузла дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Лівий дочірній вузол
        self.right = None  # Правий дочірній вузол
        self.val = key  # Значення вузла
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Функція для додавання зв'язків між вузлами дерева та обчислення їх позицій для візуалізації
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додаємо вузол до графа
        graph.add_node(
            node.id, color=node.color, label=node.val
        )
        # Якщо існує лівий дочірній вузол, додаємо зв'язок
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer  # Обчислення позиції для лівого дочірнього вузла
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        # Якщо існує правий дочірній вузол, додаємо зв'язок
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer  # Обчислення позиції для правого дочірнього вузла
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()  # Створення орієнтованого графа для дерева
    pos = {tree_root.id: (0, 0)}  # Початкова позиція кореня
    tree = add_edges(tree, tree_root, pos)  # Додавання зв'язків та позицій вузлів

    colors = [node[1]["color"] for node in tree.nodes(data=True)]  # Отримуємо кольори вузлів
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Створюємо мітки для вузлів

    # Малюємо дерево з використанням NetworkX та Matplotlib
    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()

# Функція для виконання heapify (перетворення в купу)
def heapify(arr, n, i):
    largest = i  # Ініціалізуємо найбільший як корінь
    l = 2 * i + 1  # лівий = 2*i + 1
    r = 2 * i + 2  # правий = 2*i + 2

    # Якщо лівий дочірній елемент більший за корінь
    if l < n and arr[i] < arr[l]:
        largest = l

    # Якщо правий дочірній елемент більший за найбільший елемент на даний момент
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Якщо найбільший не корінь
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Заміна

        # Перетворюємо в піддереві, яке постраждало від заміни
        heapify(arr, n, largest)

# Функція для побудови купи
def build_heap(arr):
    n = len(arr)
    # Ініціалізація як max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Функція для перетворення масиву в дерево бінарної купи
def array_to_heap_tree(arr):
    if not arr:
        return None
    n = len(arr)
    build_heap(arr)  # Створення купи з масиву

    nodes = [Node(arr[i]) for i in range(n)]  # Створення вузлів дерева
    for i in range(n // 2):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0]  # Повертаємо корінь дерева

# Головна функція для виконання
def main():
    arr = [100, 19, 36, 17, 3, 25, 1, 2, 7]  # Масив для побудови купи
    root = array_to_heap_tree(arr)  # Перетворення масиву в дерево бінарної купи
    draw_tree(root)  # Візуалізація дерева

# Запуск програми
if __name__ == "__main__":
    main()
