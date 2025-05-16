# Ветка `graphs_implementation`

**Описание**: Реализация графовых структур, алгоритмов анализа и визуализации характеристик.

## Основная функциональность

- **Представление графа** в виде классов (хранение структуры, атрибутов, методов построения)
- **Вычисление характеристик** (максимальная/минимальная степень, кликовое число и др.)
- **Визуализация статистик** (гистограммы, распределения характеристик при варьировании параметров)
- **Построение критической области** и оценки ошибок первого рода/мощностей

## Структура кода

```text
/src
  /graph.py                         # Основной класс графа
  /graph_characteristic.py          # Вычисление характеристик
  /graph_characteristic_test.py     # Тесты для вычисления характеристик
  /graph_simulate_statistics.py     # отрисовка графиков и статистик
  /graph_implementation.ipynb       # Весь код в красивом Jupiter ноутбуке с комментариями
```

## UML-диаграмма класса Graph

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ffd8d8'}}}%%
classDiagram
    class Graph {
        -V: np.ndarray[float]
        -E: list[tuple[int, int]]
        -nx_obj: nx.Graph
        
        +__init__(points: np.ndarray[float], edges: set[tuple[int, int]])
        +build_KNN_graph(K: int) void
        +build_dist_graph(max_dist: int) void
        +draw() void
    }
```
