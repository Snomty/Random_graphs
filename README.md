# Исследование зависимостей характеристик графа от распределений и создание классификатора

Проект посвящен анализу влияния различных распределений на характеристики графов и разработке классификатора, определяющего тип распределения по свойствам графа.

## Участники проекта :

- Иванова Анастасия

- Минаков Даниил


## Ветки разработки

- **`Ivanova/graph-implementation`** - Основные эксперименты и разработка
- **`Minacov/Part-I`** - Исследования по первой части
- **`Minacov/Part-II`** - Исследования по второй части (классификация)


[![CI](https://github.com/Snomty/Random_graphs/actions/workflows/ci.yml/badge.svg)](https://github.com/Snomty/Random_graphs/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

## Техническая документация

Файл [report/documentation.md](https://github.com/Snomty/Random_graphs/blob/cleanup/repository/report/documentation.md)

В ней так же указан пример использования

## Общая структура репозитория

- `.github/workflows/ci.yml` — конфигурация CI/CD (автоматические тесты при пулл-реквестах).

- `data/` — датасеты в форматах .csv, .json или других.

- `report/`

  -`report.pdf` — финальный отчет по проекту (анализ, графики, выводы).

  -`report/` — исходные файлы отчета в LaTeX (.tex).

  -`documentation.md` - документация к проекту

- `src/` — исходный код:

  - `Jupyter Notebook` (.ipynb) с исследованием и визуализацией.

  - Модули (.py) с функциями, которые используются в ноутбуках.

- `tests/` — юнит-тесты для проверки кода (написаны с помощью pytest).

