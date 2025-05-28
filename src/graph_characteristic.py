from graph import *


def calculate_min_deg(G: Graph) -> int:
    """ Возвращает минимальную степень вершин графа """
    return min(dict(G.nx_obj.degree()).values())

def calculate_max_deg(G: Graph) -> int:
    """ Возвращает максимальную степень вершин графа """
    return max(dict(G.nx_obj.degree()).values())

def calculate_number_component(G: Graph) -> int:
    """ Возвращает число компонент связности графа """
    return nx.number_connected_components(G.nx_obj)

def calculate_number_articul(G: Graph) -> int:
    """ Возвращает число точек сочленения графа """
    return len(list(nx.articulation_points(G.nx_obj)))

def calculate_number_triangle(G: Graph) -> int:
    """ Возвращает число треугольников графа """
    triangles_dict = nx.triangles(G.nx_obj)
    return sum(triangles_dict.values()) // 3

def calculate_clique_number(G: Graph) -> int:
    """ Возвращает оценку кликового числа через жадную раскраску """
    chromatic_number_approx = nx.coloring.greedy_color(G.nx_obj, strategy="largest_first")
    return max(chromatic_number_approx.values()) + 1

def calculate_maxsize_independed_set(G: Graph) -> int:
    """ Возвращает размер наибольшего независимого множества """
    complement_G = nx.complement(G.nx_obj)
    # Создаем временный объект Graph для вызова calculate_clique_number
    temp_graph = Graph(np.zeros(len(complement_G.nodes())))
    temp_graph.nx_obj = complement_G
    return calculate_clique_number(temp_graph)

human_readable_characts = {
    "calculate_min_deg": "Минимальная степень вершины",
    "calculate_max_deg": "Максимальная степень вершины",
    "calculate_number_component": "Количество компонент связности",
    "calculate_number_articul": "Количество точек сочленения",
    "calculate_number_triangle": "Количество треугольников",
    "calculate_clique_number": "Кликовое число",
    "calculate_maxsize_independed_set": "Размер наибольшего независимого множества"
}