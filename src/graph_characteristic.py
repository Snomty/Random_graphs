from graph import *

def calculate_min_deg(G: Graph) -> int:
    """ Возвращает минимальную степень вершин графа """
    min_degree_node, min_degree = min(G.nx_obj.degree(), key=lambda x: x[1])
    return min_degree

def calculate_max_deg(G: Graph) -> int:
    """ Возвращает максимальную степень вершин графа """
    max_degree_node, max_degree = max(G.nx_obj.degree(), key=lambda x: x[1])
    return max_degree

def calculate_number_component(G: Graph) -> int:
    """ Возвращает число компонент связности графа """
    return nx.number_connected_components(G.nx_obj)

def calculate_number_articul(G: Graph) -> int:
    """ Возвращает число точек сочленения графа """
    return len(list(nx.articulation_points(G.nx_obj)))

def calculate_number_triangle(G: Graph) -> int:
    """ Возвращает число треугольников графа """
    triangles_dict =  nx.triangles(G.nx_obj)
    return sum(triangles_dict.values()) // 3

def calculate_clique_number(G: Graph) -> int:
    """ Возвращает кликовое число графа """
    max_cliques = list(nx.find_cliques(G.nx_obj))
    return max([len(clique) for clique in max_cliques])

def calculate_maxsize_independed_set(G: Graph) -> int:
    """ Возвращает размер максимального независимого множества """
    V_compl = G.V
    E_compl = set()
    existing_edges = {tuple(edge) for edge in G.E}

    for i in range(len(G.V)):
        for j in range(i + 1, len(G.V)):
            if (i, j) not in existing_edges and (j, i) not in existing_edges:
                E_compl.add((i, j))

    G_compl = Graph(V_compl, E_compl)
    return calculate_clique_number(G_compl)

human_readable_characts = {"calculate_min_deg": "Минимальная степень вершины",
                           "calculate_max_deg": "Максимальная степень вершины",
                           "calculate_number_component": "Количество компонент связности",
                           "calculate_number_articul": "Количество точек сочленения",
                           "calculate_number_triangle": "Количество треугольников",
                           "calculate_clique_number": "Кликовое число",
                           "calculate_maxsize_independed_set": "Размер наибольшего независимого множества" }
