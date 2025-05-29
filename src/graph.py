import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from typing import Set, Tuple, List

class Graph:
    def __init__(self, points: np.ndarray, edges: Set[Tuple[int, int]] = None) -> None:
        self.V = points
        self.E = set([tuple(sorted(edge)) for edge in edges]) if edges else set()
        self.nx_obj = nx.Graph()
        self.nx_obj.add_nodes_from(range(len(points)))
        if edges:
            self.nx_obj.add_edges_from(edges)

    def build_KNN_graph(self, K: int) -> None:
        """ Строит ребра KNN графа """
        self.E = set()

        for idx_1, x_1 in enumerate(self.V):
            dist = []
            for idx_2, x_2 in enumerate(self.V):
                dist.append((np.linalg.norm(x_1 - x_2), idx_2))
            for nearest in sorted(dist)[1:K+1]:
                self.E.add(tuple(sorted((idx_1, nearest[1]))))

        self.nx_obj.clear_edges()
        self.nx_obj.add_edges_from(self.E)

    def build_dist_graph(self, max_dist: float) -> None:
        """ Строит ребра Distance графа """
        self.E = set()

        for idx_1, x_1 in enumerate(self.V):
            for idx_2, x_2 in enumerate(self.V):
                if idx_2 > idx_1 and np.linalg.norm(x_1 - x_2) <= max_dist:
                    self.E.add((idx_1, idx_2))

        self.nx_obj.clear_edges()
        self.nx_obj.add_edges_from(self.E)

    def draw(self) -> None:
        """ Рисует граф """
        if len(self.V) == 0:
            print("Пустой граф.")
            return

        pos = {i: (self.V[i], i) for i in range(len(self.V))}
        nx.draw(self.nx_obj, pos=pos, with_labels=True)
        plt.title("Наш граф")
        plt.xlabel("Координата")
        plt.ylabel("Номер вершины")
        plt.show()