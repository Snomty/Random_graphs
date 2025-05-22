from graph import *
from graph_characteristic import *
from typing import Callable
from scipy.stats import skewnorm
import pandas as pd
from tqdm import tqdm


skew_alpha = 1
laplace_alpha = 0
laplace_beta = 1 / np.sqrt(2)

WEIBULL_K_0 = 0.5
WEIBULL_LAMBDA_0 = 1 / np.sqrt(10)

GAMMA_K_0 = 0.5
GAMMA_LAMBDA_0 = 1 / np.sqrt(2)

def gen_skewnormal_points(num_points: int, alpha: float = skew_alpha) -> np.ndarray[np.float64]:
    """ Возвращает num_points точек сгенерированных по косому нормальному распределению S(alpha) """
    return skewnorm.rvs(alpha, size=num_points)

def gen_laplace_points(num_points: int, alpha: float = laplace_alpha, beta : float = laplace_beta) -> np.ndarray[np.float64]:
    """ Возвращает num_points точек сгенерированных по распределению Лапласа L(alpha, beta) """
    return np.random.laplace(loc=alpha, scale=beta, size=num_points)

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
        plt.xticks([ ((5 - k) * min(bins) + k * max(bins)) // 5 for k in range(6) ])
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
        plt.xticks([ ((5 - k) * min(bins) + k * max(bins)) // 5 for k in range(6) ])
        plt.xlabel("Значение характеристики")
        plt.ylabel("Количество графов")
        plt.legend()

        plt.show()
        print()

    return { "T_knn_gamma_lists": T_knn_gamma_list,
             "T_knn_weibull_lists": T_knn_weibull_list,
             "T_dist_gamma_lists": T_dist_gamma_list,
             "T_dist_weibull_lists": T_dist_weibull_list }


def build_critical_region(
        points_generator: Callable[[int], int],
        T_foo: Callable[[Graph], int] ,
        num_samples: int = 10**3, 
        alpha: float = 0.05) -> int:
    """Построение критической области A_crit."""
    A_values = []
    for _ in range(num_samples):
        G_dist = Graph(points = points_generator(50))
        G_dist.build_dist_graph(max_dist = 1)
        A = T_foo(G_dist)
        A_values.append(A)

    A_crit = np.percentile(A_values, 100 * (1 - alpha))
    return int(np.ceil(A_crit))


def estimate_power(
        points_generator_1: Callable[[int], int],
        points_generator_2: Callable[[int], int],
        T_foo: Callable[[Graph], int] ,
        A_crit: int, 
        num_samples: int = 10**4
    ) -> float:
    """Оценка мощности критерия."""

    H1_counter = 0
    H0_counter = 0
    for _ in range(num_samples):
        G_dist = Graph(points = points_generator_2(50))
        G_dist.build_dist_graph(max_dist = 1)
        A = T_foo(G_dist)
        if A > A_crit:  # Отвергаем H_0
            H1_counter += 1
    power = H1_counter / num_samples

    for _ in range(num_samples):
        G_dist = Graph(points = points_generator_1(50))
        G_dist.build_dist_graph(max_dist = 1)
        A = T_foo(G_dist)
        if A <= A_crit:  # Принимаем H_0
            H0_counter += 1
    approved = H0_counter / num_samples

    return power, approved


def generate_dataset(
    points_generator_1: Callable[[int], int],
    points_generator_2: Callable[[int], int], 
    num_vertex : int = 25, 
    dataset_size : int = 10000,
    max_dist : int = 1
) -> pd.DataFrame:

    distribution_1_characteristics = []
    distribution_2_characteristics = []

    characteristics_functions = [
        calculate_min_deg, calculate_max_deg, calculate_number_component, calculate_number_articul,
        calculate_number_triangle, calculate_clique_number, calculate_maxsize_independed_set
    ]
    
    characteristics_names = [
       'min_deg', 'max_deg', 'number_component', 'number_articul', 
       'numbertriangle', 'clique_number', 'max_independent_set'
    ]
    
    dataset_size = dataset_size // 2
    for _ in tqdm(range(dataset_size)):
        first_distribution = Graph(points = points_generator_1(num_vertex))
        first_distribution.build_dist_graph(max_dist = max_dist)

        second_distribution = Graph(points = points_generator_2(num_vertex))
        second_distribution.build_dist_graph(max_dist = max_dist)

        first = []
        second = []
        for func in characteristics_functions:
          first.append(func(first_distribution))
          second.append(func(second_distribution))

        distribution_1_characteristics.append(first)
        distribution_2_characteristics.append(second)

    distribution_1_characteristics = pd.DataFrame(distribution_1_characteristics, columns=characteristics_names)
    distribution_2_characteristics = pd.DataFrame(distribution_2_characteristics, columns=characteristics_names)

    distribution_1_characteristics['distribution'] = 0
    distribution_2_characteristics['distribution'] = 1

    df = pd.concat([distribution_1_characteristics, distribution_2_characteristics], ignore_index=True)
    df = df.sample(frac=1).reset_index(drop=True)

    return df
