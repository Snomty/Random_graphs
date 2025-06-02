# Техническая документация: Анализ графовых структур

## Содержание
1. [Класс Graph](#класс-graph)
2. [Характеристики графа](#характеристики-графа)
3. [Симуляция статистик](#симуляция-статистик)
4. [Генерация данных](#генерация-данных)
5. [Визуализация](#визуализация)
---
Чтобы собрать проект, совершите следующие действия:

- склонируйте репозиторий и перейдите в него 
  - git clone https://github.com/Snomty/Random_graphs.git 
  - cd Random_graphs
- в командной строке пропишите pip3 install -e .
---

## Для работы требуется:

- Python 3.8+

- Библиотеки: `networkx`, `numpy`, `matplotlib`, `scipy`

- Все распределения генерируются с предустановленными параметрами

- Визуализация поддерживает настройку через параметры функций
---
## Класс Graph
`graph.py` - реализация графовой структуры с методами построения и визуализации.

### Инициализация
```python
Graph(points: np.ndarray, edges: Set[Tuple[int, int]] = None)
```
points: массив координат вершин (N x d)

edges: множество ребер (опционально)

Методы
|Метод|Описание|Параметры|Возвращаемое значение|
|-----|--------|---------|---------------------|
|build_KNN_graph(K)|Строит K-ближайших соседей|	K: число соседей	|-|
|build_dist_graph(max_dist)|Строит граф по расстоянию	|max_dist: порог расстояния	|-|
|draw()|Визуализирует граф	|-	|-|

```python
points = np.random.rand(10, 2)
g = Graph(points)
g.build_KNN_graph(3)
g.draw()
```

## Характеристики графа
`graph_characteristics.py` - вычисление метрик графа.

### Доступные метрики:
- Минимальная степень вершины (calculate_min_deg)

- Максимальная степень вершины (calculate_max_deg)

- Число компонент связности (calculate_number_component)

- Число точек сочленения (calculate_number_articul)

- Число треугольников (calculate_number_triangle)

- Кликовое число (calculate_clique_number)

- Размер наибольшего независимого множества (calculate_maxsize_independed_set)

Пример:

```python
g = Graph(points)
print(calculate_number_triangle(g))  # Выводит количество треугольников
```

## Симуляция статистик
`graph_simulate_statistics.py` - анализ графов для разных распределений.

## Основные функции:

```python
simulate_graph_statistics(
    num_samples=420,
    vector_size=42,
    distribution_type="gamma_weibull",
    ...
)
```

Параметры:

- `distribution_type`: "gamma_weibull" или "laplace_skewnormal"

- `T_knn_foo`: характеристика для KNN-графа

- `T_dist_foo`: характеристика для distance-графа

Возвращает:
Словарь с распределениями характеристик для каждого типа графа.

## Критические области:
```python
build_critical_region(points_generator, T_foo, num_samples=1000, alpha=0.05)
```

## Генерация данных
### Формирование датасета:
```python
generate_dataset(
    points_generator_1,
    points_generator_2,
    num_vertex=25,
    dataset_size=10000
)
```
## Визуализация

### Сравнение распределений:

```python
plot_distribution_parameter_combinations(
    laplace_alphas=[0],
    laplace_betas=[1/np.sqrt(2)],
    skew_norm_alphas=[1]
)
```

Строит гистограммы характеристик для разных параметров.

### Параметрический анализ:
```python
plot_graphs_parameter_combinations(
    sizes=[40],
    neighbours=[3],
    dists=[1],
    graph_type="knn"
)
```
## Пример полного цикла
```python
from graph import Graph
from graph_characteristics import calculate_number_triangle
from graph_simulate_statistics import gen_gamma_points, simulate_graph_statistics

# 1. Генерация данных
points = gen_gamma_points(50)

# 2. Построение графа
g = Graph(points)
g.build_dist_graph(max_dist=1.5)

# 3. Анализ
print("Треугольников:", calculate_number_triangle(g))

# 4. Статистический анализ
results = simulate_graph_statistics(
    T_knn_foo=calculate_number_triangle,
    T_dist_foo=calculate_number_triangle
)
```
