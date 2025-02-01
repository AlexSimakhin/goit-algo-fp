"""task3.py"""
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Список вершин (зірок) і їх позицій
stars = {
    "Сонце": (5, 7),
    "Альфа Центавра": (3.5, 9.3),
    "Вега": (3, 10),
    "Сіріус": (1, 2),
    "Проціон": (2, 7),
    "Бетельгейзе": (7, 9),
    "Ріґель": (4, 3),
    "Альдебаран": (9, 6),
    "Капела": (5.5, 8.6),
    "Планета X": (6.5, 6.5),
}

# Ребра між вершинами (зв'язки між зірками) з вагами
edges = [
    ("Сонце", "Альфа Центавра", 5),
    ("Альфа Центавра", "Вега", 2),
    ("Вега", "Проціон", 6),
    ("Проціон", "Сонце", 7),
    ("Сонце", "Сіріус", 3),
    ("Сіріус", "Ріґель", 4),
    ("Ріґель", "Альдебаран", 8),
    ("Альдебаран", "Бетельгейзе", 10),
    ("Сонце", "Планета X", 9),
    ("Планета X", "Альдебаран", 3),
    ("Сонце", "Капела", 2),
    ("Капела", "Бетельгейзе", 4),
]

# Додавання вершин до графа з координатами
for star, pos in stars.items():
    G.add_node(star, pos=pos)
    
# Додавання ребер з вагами до графа
G.add_weighted_edges_from(edges)

# Оновлена функція Дейкстри, що використовує бінарну купу для оптимізації
def dijkstra(graph, start):
    # Ініціалізуємо відстані до всіх вершин як нескінченність
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0  # Початкова вершина має відстань 0
    priority_queue = [(0, start)]  # Черга з пріоритетом із початковою вершиною

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Пропускаємо, якщо знайдений кращий шлях
        if current_distance > distances[current_node]:
            continue

        # Перевіряємо всіх сусідів поточного вузла
        for neighbor, attributes in graph[current_node].items():
            weight = attributes["weight"]  # Вага ребра
            distance = current_distance + weight  # Новий шлях

            # Оновлення найкращої відстані
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Функція для обчислення відстаней залежно від вибору користувача
def calculate_distances(option, start_planet=None):
    if option == "single" and start_planet:
        # Обчислення для однієї обраної планети
        distances_from_start = dijkstra(G, start_planet)
        print(f"\nНайкоротші шляхи від '{start_planet}':")
        for target, distance in distances_from_start.items():
            print(f"Від '{start_planet}' до {target}: відстань {distance}")
    elif option == "all":
        # Обчислення для всіх планет
        print("\nНайкоротші шляхи для всіх планет:")
        for planet in stars.keys():
            distances_from_planet = dijkstra(G, planet)
            print(f"\nВід '{planet}':")
            for target, distance in distances_from_planet.items():
                print(f"  до {target}: відстань {distance}")
    else:
        print("Неправильний вибір опції!")

# Запит користувача щодо вибору
option = input("Обчислити відстань для однієї планети чи для всіх? (введіть 'single' або 'all'): ").strip().lower()

if option == "single":
    start_planet = input("Введіть назву планети (Доступні: \n" + ", ".join(stars.keys()) + "): ").strip()
    if start_planet in stars:
        calculate_distances(option, start_planet)
    else:
        print("Планета не знайдена!")
elif option == "all":
    calculate_distances(option)
else:
    print("Некоректний вибір!")

# Візуалізація графа з вагою ребер
pos = nx.get_node_attributes(G, "pos")
plt.figure(figsize=(8, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="yellow",
    edge_color="cyan",
    node_size=1200,
    font_size=10,
    font_color="black",
)

# Показ ваги ребер на графі
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Назва графіка
plt.title("Модель зоряної мережі з вагами на ребрах", fontsize=14, color="black")
plt.gca().set_facecolor("black")
plt.show()
