# Ветка `Minacov/Part-II`

**Описание**: Создание классификатора распределения на основе характеристик графа.

## Структура кода

```text
/data
  /df_25_vert_Student2.csv                          # Датасет для графа на 25 вершинах
  /df_100_vert_Student2.csv                         # Датасет для графа на 100 вершинах
  /df_500_vert_Student2.csv                         # Датасет для графа на 500 вершинах
/src
  /graph.py                                         # Основной класс графа
  /graph_characteristic.py                          # Вычисление характеристик
  /graph_simulate_statistics.py                     # Вспомогательные функции
  /Graph_Hypothesis_Classifier_Student2.ipynb       # Весь код в красивом Jupiter ноутбуке с комментариями
```