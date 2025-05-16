import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, points: np.ndarray[float], edges: set[tuple[int, int]] = set()) -> None:
        self.V = points
        self.E = [sorted(edge) for edge in edges]
        self.nx_obj = nx.empty_graph(len(points))
        self.nx_obj.add_edges_from(edges)


    def build_KNN_graph(self, K: int) -> None:
        """ Строит ребра KNN графа """
        self.E = set()

        for idx_1, x_1 in enumerate(self.V):
            dist = []
            for idx_2, x_2 in enumerate(self.V):
                dist.append([np.linalg.norm(x_1 - x_2), idx_2])
            for nearest in sorted(dist)[1:K+1]:
                self.E.add( (min(idx_1, nearest[1]), max(idx_1, nearest[1])) )

        self.nx_obj.clear_edges()
        self.nx_obj.add_edges_from(self.E)

    def build_dist_graph(self, max_dist: int) -> None:
        """ Строит ребра Distance графа """
        self.E = set()

        for idx_1, x_1 in enumerate(self.V):
            dist = []
            for idx_2, x_2 in enumerate(self.V):
                if (idx_2 <= idx_1):
                    continue
                if np.linalg.norm(x_1 - x_2) <= max_dist:
                    self.E.add( (idx_1, idx_2) )

        self.nx_obj.clear_edges()
        self.nx_obj.add_edges_from(self.E)

    def draw(self) -> None:
        """ Рисует граф """
        if (len(self.V) == 0):
            print("Пустой граф.")
            return

        for e in self.E:
            x1, y1 = self.V[e[0]], e[0]
            x2, y2 = self.V[e[1]], e[1]
            plt.plot([x1, x2], [y1, y2], 'b-', linewidth=1)
        plt.scatter(self.V, range(len(self.V)), color="blue")
        plt.title("Наш граф")
        plt.xlabel("Ее координата")
        plt.ylabel("Номер вершины")
        