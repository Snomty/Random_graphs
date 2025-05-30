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
        num_samples: int = 420,                                 # количество реализаций характеристики
        vector_size: int = 42,                                  # размерность случайного вектора
        distribution_type: str = "gamma_weibull",   # тип используемых распределений
        # Параметры распределений
        gamma_k: float = 0.5,                                   # параметр k гамма-распределения
        gamma_lambda: float = 1/np.sqrt(2),                      # параметр lambda гамма-распределения
        weibull_k: float = 0.5,                                 # параметр k распределения Вейбулла
        weibull_lambda: float = 1/np.sqrt(10),                   # параметр lambda распределения Вейбулла
        skew_alpha: float = 1,                                  # параметр alpha косого нормального распределения
        laplace_alpha: float = 0,                               # параметр alpha распределения Лапласа
        laplace_beta: float = 1/np.sqrt(2),                      # параметр beta распределения Лапласа
        # Параметры графов
        T_knn_foo: Callable[[Graph], int] = calculate_number_triangle,   # функция для KNN графа
        knn_num_neighbours: int = 42,                           # количество соседей KNN графа
        T_dist_foo: Callable[[Graph], int] = calculate_maxsize_independed_set,  # функция для Distance графа
        dist_max_dist: float = 4.2,                             # максимальная длина соединения Distance графа
        verbose: bool = False                                   # рисовать ли гистограммы
) -> dict:
    """
    Универсальная функция для симуляции статистик графов с разными распределениями.
    
    Параметры:
    - distribution_type: "gamma_weibull" или "laplace_skewnormal" - тип используемых распределений
    """
    # Инициализация списков для результатов
    T_knn_dist1_list, T_knn_dist2_list = [], []
    T_dist_dist1_list, T_dist_dist2_list = [], []
    
    # Генераторы точек в зависимости от типа распределения
    if distribution_type == "gamma_weibull":
        gen_dist1 = lambda n: np.random.gamma(gamma_k, gamma_lambda, n)
        gen_dist2 = lambda n: weibull_lambda * np.random.weibull(weibull_k, n)
        dist1_name = "Гамма распределение"
        dist2_name = "Распределение Вейбулла"
        dist1_params = f"Г( {gamma_k}, {gamma_lambda} )"
        dist2_params = f"Weibull( {weibull_k}, {weibull_lambda} )"
    else:
        gen_dist1 = lambda n: skewnorm.rvs(skew_alpha, size=n)
        gen_dist2 = lambda n: np.random.laplace(loc=laplace_alpha, scale=laplace_beta, size=n)
        dist1_name = "Косое нормальное распределение"
        dist2_name = "Распределение Лапласа"
        dist1_params = f"Skewnormal( {skew_alpha} )"
        dist2_params = f"Laplace( {laplace_alpha}, {laplace_beta} )"

    for _ in range(num_samples):
        # Генерация точек
        dist1_sample = gen_dist1(vector_size)
        dist2_sample = gen_dist2(vector_size)

        # Обработка KNN графов
        G_knn_dist1 = Graph(points=dist1_sample)
        G_knn_dist1.build_KNN_graph(K=knn_num_neighbours)
        T_knn_dist1_list.append(T_knn_foo(G=G_knn_dist1))

        G_knn_dist2 = Graph(points=dist2_sample)
        G_knn_dist2.build_KNN_graph(K=knn_num_neighbours)
        T_knn_dist2_list.append(T_knn_foo(G=G_knn_dist2))

        # Обработка Distance графов
        G_dist_dist1 = Graph(points=dist1_sample)
        G_dist_dist1.build_dist_graph(max_dist=dist_max_dist)
        T_dist_dist1_list.append(T_dist_foo(G=G_dist_dist1))

        G_dist_dist2 = Graph(points=dist2_sample)
        G_dist_dist2.build_dist_graph(max_dist=dist_max_dist)
        T_dist_dist2_list.append(T_dist_foo(G=G_dist_dist2))

    if verbose:
        plt.figure(figsize=(16, 3))

        # KNN график
        plt.subplot(1, 2, 1)
        bins = np.arange(min(T_knn_dist1_list + T_knn_dist2_list),
                         max(T_knn_dist1_list + T_knn_dist2_list) + 1, 1)
        plt.hist(T_knn_dist1_list, bins=bins, align="mid", alpha=0.5, label=dist1_name)
        plt.hist(T_knn_dist2_list, bins=bins, align="mid", alpha=0.5, label=dist2_name)
        plt.title(
            f"Распределение характеристики '{human_readable_characts[T_knn_foo.__name__]}'\n"
            f"KNN граф. K={knn_num_neighbours}. Размерность={vector_size}\n\n"
            f"{dist2_params}\n{dist1_params}"
        )
        plt.xticks(bins)
        plt.xlabel("Значение характеристики")
        plt.ylabel("Количество графов")
        plt.legend()

        # Distance график
        plt.subplot(1, 2, 2)
        bins = np.arange(min(T_dist_dist1_list + T_dist_dist2_list),
                         max(T_dist_dist1_list + T_dist_dist2_list) + 1, 1)
        plt.hist(T_dist_dist1_list, bins=bins, align="mid", alpha=0.5, label=dist1_name)
        plt.hist(T_dist_dist2_list, bins=bins, align="mid", alpha=0.5, label=dist2_name)
        plt.title(
            f"Распределение характеристики '{human_readable_characts[T_dist_foo.__name__]}'\n"
            f"Distance граф. max_dist={dist_max_dist}. Размерность={vector_size}\n\n"
            f"{dist2_params}\n{dist1_params}"
        )
        plt.xticks(bins)
        plt.xlabel("Значение характеристики")
        plt.ylabel("Количество графов")
        plt.legend()

        plt.show()

    # Возвращаем результаты в соответствующем формате
    if distribution_type == "gamma_weibull":
        return {
            "T_knn_gamma_lists": T_knn_dist1_list,
            "T_knn_weibull_lists": T_knn_dist2_list,
            "T_dist_gamma_lists": T_dist_dist1_list,
            "T_dist_weibull_lists": T_dist_dist2_list
        }
    else:
        return {
            "T_knn_skew_normal_list": T_knn_dist1_list,
            "T_knn_laplace_list": T_knn_dist2_list,
            "T_dist_skew_normal_list": T_dist_dist1_list,
            "T_dist_laplace_list": T_dist_dist2_list
        }


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
        T_foo: Callable[[Graph], int],
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


# перебор параметров распределений и вывод соответствующих графиков
def plot_distribution_parameter_combinations(laplace_alphas, laplace_betas, skew_norm_alphas,
                               num_samples=200, vector_size=40,
                               knn_num_neighbours=3, dist_max_dist=1, graph_type : str = "knn"):
    # laplace_alphas - значение первого параметра распределения лапласа
    # laplace_betas - значения второго параметра распределения лапласа
    # skew_norm_alphas - значения параметра косого распределения
    plot_counter = 0
    plt.figure(figsize=(24, 6))

    for alpha in laplace_alphas:
        for beta in laplace_betas:
            for alpha_skew in skew_norm_alphas:
                if plot_counter % 4 == 0 and plot_counter != 0:
                    plt.tight_layout()
                    plt.show()
                    plt.figure(figsize=(24, 6))

                result = simulate_graph_statistics(
                    num_samples=num_samples,
                    vector_size=vector_size,
                    verbose=False,
                    knn_num_neighbours=knn_num_neighbours,
                    dist_max_dist=dist_max_dist,
                    laplace_alpha=alpha,
                    laplace_beta=beta,
                    skew_alpha=alpha_skew,
                    distribution_type="laplace_skew"
                )

                plt.subplot(2, 8, 2*(plot_counter % 4) + 1)
                bins = np.arange(min(result["T_knn_skew_normal_list"] + result["T_knn_laplace_list"]),
                                max(result["T_knn_skew_normal_list"] + result["T_knn_laplace_list"]) + 1, 1)
                plt.hist(result["T_knn_skew_normal_list"], bins=bins, align="mid", alpha=0.5, label="Косое нормальное")
                plt.hist(result["T_knn_laplace_list"], bins=bins, align="mid", alpha=0.5, label="Лаплас")
                plt.title(f"KNN\nα={alpha}, β={beta}\nskew={alpha_skew}", fontsize=10)
                plt.legend(fontsize=8)

                plt.subplot(2, 8, 2*(plot_counter % 4) + 2)
                bins = np.arange(min(result["T_dist_skew_normal_list"] + result["T_dist_laplace_list"]),
                                max(result["T_dist_skew_normal_list"] + result["T_dist_laplace_list"]) + 1, 1)
                plt.hist(result["T_dist_skew_normal_list"], bins=bins, align="mid", alpha=0.5, label="Косое нормальное")
                plt.hist(result["T_dist_laplace_list"], bins=bins, align="mid", alpha=0.5, label="Лаплас")
                plt.title(f"Distance\nα={alpha}, β={beta}\nskew={alpha_skew}", fontsize=10)
                plt.legend(fontsize=8)

                plot_counter += 1


    if plot_counter % 4 != 0 or plot_counter == 0:
        plt.tight_layout()
        plt.show()


#  перебор параметров для построения графа и вывод соответствующих графиков
def plot_graphs_parameter_combinations(sizes : np.ndarray[float] = [40], neighbours : np.ndarray[float] = [3], dists :  np.ndarray[float] = [1],  graph_type : str = "knn"):
  # sizes - размер графа
  # neighbours - кол-во соседей в knn
  # dists - расстояние для дист.графа
  # graph_type - какой график отрисовывать knn или dist
  plot_counter = 0
  plt.figure(figsize=(24, 4))
  for n in sizes:
      for neigh in neighbours:
          for dist in dists:
            result = simulate_graph_statistics(
                num_samples=200,
                vector_size=n,
                verbose=False,
                knn_num_neighbours=neigh,
                dist_max_dist=dist,
                distribution_type="laplace_skew"
            )

            if plot_counter % 8 == 0 and plot_counter != 0:
                plt.tight_layout()
                plt.show()
                plt.figure(figsize=(24, 4))

            plt.subplot(1, 8, (plot_counter % 8) + 1)
            bins = np.arange(min(result[f"T_{graph_type}_skew_normal_list"] + result[f"T_{graph_type}_laplace_list"]),
                          max(result[f"T_{graph_type}_skew_normal_list"] + result[f"T_{graph_type}_laplace_list"]) + 1, 1)
            plt.hist(result[f"T_{graph_type}_skew_normal_list"], bins=bins, align="mid", alpha=0.5, label="Skew normal")
            plt.hist(result[f"T_{graph_type}_laplace_list"], bins=bins, align="mid", alpha=0.5, label="Laplace")

            # Упрощенный заголовок
            plt.title(f"Size={n}\nparameter={neigh}\n{graph_type}\ndisatnce = {dist}", fontsize=9)
            plt.xlabel("Value", fontsize=8)
            plt.ylabel("Count", fontsize=8)

            plot_counter += 1

  # Отображаем последние графики, если они есть
  if plot_counter % 8 != 0:
      plt.tight_layout()
      plt.show()
