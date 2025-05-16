from graph import *
from graph_characteristic import *
from typing import Callable


WEIBULL_K_0 = 0.5
WEIBULL_LAMBDA_0 = 1 / np.sqrt(10)

GAMMA_K_0 = 0.5
GAMMA_LAMBDA_0 = 1 / np.sqrt(2)

def gen_weibull_points(num_points: int, k: float = WEIBULL_K_0, lambd: float = WEIBULL_LAMBDA_0) -> np.ndarray[np.float64]:
    """ Возвращает num_points точек сгенерированных по распределению Вейбулла W(k, lambd) """
    return lambd * np.random.weibull(k, num_points)


def gen_gamma_points(num_points: int, k: float = GAMMA_K_0, lambd: float = GAMMA_LAMBDA_0) -> np.ndarray[np.float64]:
    """ Возвращает num_points точек сгенерированных по гамма-распределению Gamm(k, lambd)"""
    return np.random.gamma(k, lambd, num_points)


def simulate_graph_statistics(
        sample_size: int = 420,                                 # количество реализация характеристики
        vector_size: int = 42,                                  # размерность случайного вектора
        gamma_k: float = GAMMA_K_0,                             # параметр k гамма-распределения
        gamma_lambda: float = GAMMA_LAMBDA_0,                   # параметр lambda гамма-распределения
        weibull_k: float = WEIBULL_K_0,                         # параметр k распределения Вейбулла
        weibull_lambda: float = WEIBULL_LAMBDA_0,               # параметр lambda распределения Вейбулла
        T_knn_foo: Callable[[Graph], int] = calculate_max_deg,  # функция вычисления характеристики для KNN графа
        knn_num_neighbours: int = 42,                           # количество соседей KNN графа
        T_dist_foo: Callable[[Graph], int] = calculate_max_deg, # функция вычисления характеристики для Distance графа
        dist_max_dist: int = 4.2,                               # макисмальная длина соединения Distance графа
        verbose: bool = False                        # рисовать ли гистограммы распределения
) -> dict[str: list]:
    """
    Несколько раз симмулирует реализацию случайного вектора с некоторыми параметрами.
    Строит по ним KNN и Distance графы с некоторыми параметрами процедуры построения,
    вычисляет на них характеристики и визуализирует их распределение.
    Возвращает списки получившихся характеристик.
    """
    T_knn_gamma_list, T_knn_weibull_list = [], []
    T_dist_gamma_list, T_dist_weibull_list = [], []

    for i in range(sample_size):
        gamma_sample = gen_gamma_points(vector_size, gamma_k, gamma_lambda)
        weibull_sample = gen_weibull_points(vector_size, weibull_k, weibull_lambda)

        G_knn_gamma = Graph(points = gamma_sample)
        G_knn_gamma.build_KNN_graph(K = knn_num_neighbours)
        T_knn_gamma_list.append(T_knn_foo(G = G_knn_gamma))

        G_knn_weibull = Graph(points = weibull_sample)
        G_knn_weibull.build_KNN_graph(K = knn_num_neighbours)
        T_knn_weibull_list.append(T_knn_foo(G = G_knn_weibull))

        G_dist_gamma = Graph(points = gamma_sample)
        G_dist_gamma.build_dist_graph(max_dist = dist_max_dist)
        T_dist_gamma_list.append(T_dist_foo(G = G_dist_gamma))

        G_dist_weibull = Graph(points = weibull_sample)
        G_dist_weibull.build_dist_graph(max_dist = dist_max_dist)
        T_dist_weibull_list.append(T_dist_foo(G = G_dist_weibull))

    if verbose:
        plt.figure(figsize=(16, 3))


        plt.subplot(1, 2, 1)
        plt.title(f"Распределение характеристики \'{human_readable_characts[T_knn_foo.__name__]}\'\n"+
                  f"KNN граф.       K={knn_num_neighbours}.       vector dimension={vector_size}\n\n" +
                  f" Weibull( {weibull_k},  {weibull_lambda} ) \nГ( { gamma_k},  {gamma_lambda} )")
        bins = np.arange(min(T_knn_gamma_list + T_knn_weibull_list), max(T_knn_gamma_list + T_knn_weibull_list) + 1, 1)
        plt.hist(T_knn_gamma_list, bins=bins, align="mid", alpha = 0.5, label="Гамма распределение")
        plt.hist(T_knn_weibull_list, bins=bins, align="mid", alpha = 0.5, label="Распределение Вейбулла")
        plt.xticks(bins)
        plt.xlabel("Значение характеристики")
        plt.ylabel("Количество графов")
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.title(f"Распределение характеристики \'{human_readable_characts[T_dist_foo.__name__]}\'\n" +
                  f"Distance граф.       max_distance_connected={dist_max_dist}.       vector dimension={vector_size}\n\n" +
                  f"Weibull( {weibull_k},  {weibull_lambda} ) \nГ( { gamma_k},  {gamma_lambda} ) ")
        bins = np.arange(min(T_dist_gamma_list + T_dist_weibull_list), max(T_dist_gamma_list + T_dist_weibull_list) + 1, 1)
        plt.hist(T_dist_gamma_list, bins=bins, align="mid", alpha = 0.5, label="Гамма распределение")
        plt.hist(T_dist_weibull_list, bins=bins, align="mid", alpha = 0.5, label="Распределение Вейбулла")
        plt.xticks(bins)
        plt.xlabel("Значение характеристики")
        plt.ylabel("Количество графов")
        plt.legend()

        plt.show()
        print()

    return { "T_knn_gamma_lists": T_knn_gamma_list,
             "T_knn_weibull_lists": T_knn_weibull_list,
             "T_dist_gamma_lists": T_dist_gamma_list,
             "T_dist_weibull_lists": T_dist_weibull_list }


def build_critical_region(num_samples: int = 10**4, alpha: float = (0.05)**5) -> int:
    """Построение критической области A_crit."""
    A_values = []
    for _ in range(num_samples):
        dist_weibull_normal = Graph(points = gen_weibull_points(20))
        dist_weibull_normal.build_dist_graph(max_dist = 1)
        A = calculate_clique_number(dist_weibull_normal)
        A_values.append(A)

    A_crit = np.percentile(A_values, 100 * (1 - alpha))
    return int(np.ceil(A_crit))

def estimate_power(A_crit: int, num_samples: int = 10**4) -> float:
    """Оценка мощности критерия."""
    rejections = 0
    weibull = 0
    for _ in range(num_samples):
        dist_gamma = Graph(points = gen_gamma_points(20))
        dist_gamma.build_dist_graph(max_dist = 1)
        A = calculate_clique_number(dist_gamma)
        if A > A_crit:  # Отвергаем H_0
            rejections += 1
    power = rejections / num_samples

    for _ in range(num_samples):
        dist_weibull_normal = Graph(points = gen_weibull_points(20))
        dist_weibull_normal.build_dist_graph(max_dist = 1)
        A = calculate_clique_number(dist_weibull_normal)
        if A <= A_crit:  # Принимаем H_0
            weibull += 1
    approved = weibull / num_samples


    return power, approved
