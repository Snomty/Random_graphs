from graph_simulate_statistics import *

def test_calculate_min_deg():
    # Тест 1: Одна вершина без ребер
    G1 = Graph([np.array([0.0])])
    assert calculate_min_deg(G1) == 0, "Тест 1 (1 вершина без ребер) не пройден"

    # Тест 2: Две вершины без ребер
    G2 = Graph([np.array([0.0]), np.array([1.0])])
    assert calculate_min_deg(G2) == 0, "Тест 2 (2 вершины без ребер) не пройден"

    # Тест 3: Две вершины с одним ребром
    G3 = Graph([np.array([0.0]), np.array([1.0])], {(0, 1)})
    assert calculate_min_deg(G3) == 1, "Тест 3 (2 вершины с ребром) не пройден"

    # Тест 4: Треугольник (все степени равны 2)
    G4 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1), (1, 2), (2, 0)})
    assert calculate_min_deg(G4) == 2, "Тест 4 (треугольник) не пройден"

    # Тест 5: Граф с висячей вершиной
    G5 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1), (0, 2)})
    assert calculate_min_deg(G5) == 1, "Тест 5 (висячая вершина) не пройден"

    # Тест 6: Граф с изолированной вершиной
    G6 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1)})
    assert calculate_min_deg(G6) == 0, "Тест 6 (изолированная вершина) не пройден"

    # Тест 7: Граф-звезда с 4 вершинами
    G7 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (0, 2), (0, 3)})
    assert calculate_min_deg(G7) == 1, "Тест 7 (граф-звезда) не пройден"

    # Тест 8: Граф с разными степенями вершин
    G8 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (0, 2), (1, 2), (2, 3)})
    assert calculate_min_deg(G8) == 1, "Тест 8 (разные степени) не пройден"

    print("Все 8 тестов для calculate_min_deg прошли успешно!")


def test_calculate_max_deg():
    # Тест 1: Одна вершина без ребер
    G1 = Graph([np.array([0.0])])
    assert calculate_max_deg(G1) == 0, "Тест 1 (1 вершина без ребер) не пройден"

    # Тест 2: Две вершины без ребер
    G2 = Graph([np.array([0.0]), np.array([1.0])])
    assert calculate_max_deg(G2) == 0, "Тест 2 (2 вершины без ребер) не пройден"

    # Тест 3: Две вершины с одним ребром
    G3 = Graph([np.array([0.0]), np.array([1.0])], {(0, 1)})
    assert calculate_max_deg(G3) == 1, "Тест 3 (2 вершины с ребром) не пройден"

    # Тест 4: Треугольник (все степени равны 2)
    G4 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1), (1, 2), (2, 0)})
    assert calculate_max_deg(G4) == 2, "Тест 4 (треугольник) не пройден"

    # Тест 5: Граф с центральной вершиной
    G5 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1), (0, 2)})
    assert calculate_max_deg(G5) == 2, "Тест 5 (центральная вершина) не пройден"

    # Тест 6: Граф с изолированной вершиной
    G6 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1)})
    assert calculate_max_deg(G6) == 1, "Тест 6 (изолированная вершина) не пройден"

    # Тест 7: Граф-звезда с 4 вершинами
    G7 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (0, 2), (0, 3)})
    assert calculate_max_deg(G7) == 3, "Тест 7 (граф-звезда) не пройден"

    # Тест 8: Граф с разными степенями вершин
    G8 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (0, 2), (1, 2), (2, 3)})
    assert calculate_max_deg(G8) == 3, "Тест 8 (разные степени) не пройден"

    print("Все 8 тестов для calculate_max_deg прошли успешно!")


def test_calculate_number_component():
    # Тест 1: Одна вершина без ребер
    G1 = Graph([np.array([0.0])])
    assert calculate_number_component(G1) == 1, "Тест 1 (1 вершина) не пройден"

    # Тест 2: Две изолированные вершины
    G2 = Graph([np.array([0.0]), np.array([1.0])])
    assert calculate_number_component(G2) == 2, "Тест 2 (2 изолированные вершины) не пройден"

    # Тест 3: Две связанные вершины
    G3 = Graph([np.array([0.0]), np.array([1.0])], {(0, 1)})
    assert calculate_number_component(G3) == 1, "Тест 3 (2 связанные вершины) не пройден"

    # Тест 4: Три вершины, две связаны
    G4 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1)})
    assert calculate_number_component(G4) == 2, "Тест 4 (3 вершины, 2 связаны) не пройден"

    # Тест 5: Треугольник (1 компонента)
    G5 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1), (1, 2), (2, 0)})
    assert calculate_number_component(G5) == 1, "Тест 5 (треугольник) не пройден"

    # Тест 6: Две отдельные компоненты
    G6 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (2, 3)})
    assert calculate_number_component(G6) == 2, "Тест 6 (2 компоненты) не пройден"

    # Тест 7: Три компоненты (1 пара и 2 одиночные)
    G7 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(1, 2)})
    assert calculate_number_component(G7) == 3, "Тест 7 (3 компоненты) не пройден"

    # Тест 8: Сложная структура (3 компоненты)
    G8 = Graph([
        np.array([0.0]),  # компонента 1 (0-1-2)
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0]),  # компонента 2 (3-4)
        np.array([4.0]),
        np.array([5.0])   # компонента 3 (5)
    ], {(0, 1), (1, 2), (3, 4)})
    assert calculate_number_component(G8) == 3, "Тест 8 (сложная структура) не пройден"

    print("Все 8 тестов для calculate_number_component прошли успешно!")


def test_calculate_number_articul():
    # Тест 1: Две вершины, соединенные ребром (нет точек сочленения)
    G1 = Graph([np.array([0.0]), np.array([1.0])], {(0, 1)})
    assert calculate_number_articul(G1) == 0, "Тест 1 (2 связанные вершины) не пройден"

    # Тест 2: Три вершины в цепочке (центральная - точка сочленения)
    G2 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1), (1, 2)})
    assert calculate_number_articul(G2) == 1, "Тест 2 (цепочка из 3 вершин) не пройден"

    # Тест 3: Треугольник (нет точек сочленения)
    G3 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1), (1, 2), (2, 0)})
    assert calculate_number_articul(G3) == 0, "Тест 3 (треугольник) не пройден"

    # Тест 4: Граф-звезда (центр - точка сочленения)
    G4 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (0, 2), (0, 3)})
    assert calculate_number_articul(G4) == 1, "Тест 4 (граф-звезда) не пройден"

    # Тест 5: Две компоненты, каждая с точкой сочленения
    G5 = Graph([
        np.array([0.0]),  # компонента 1 (0-1-2)
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0]),  # компонента 2 (3-4-5)
        np.array([4.0]),
        np.array([5.0])
    ], {(0, 1), (1, 2), (3, 4), (4, 5)})
    assert calculate_number_articul(G5) == 2, "Тест 5 (2 компоненты) не пройден"

    # Тест 6: Граф с двумя точками сочленения
    G6 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0]),
        np.array([4.0])
    ], {(0, 1), (1, 2), (2, 3), (3, 4), (1, 3)})
    assert calculate_number_articul(G6) == 2, "Тест 6 (2 точки сочленения) не пройден"

    # Тест 7: Граф без точек сочленения (все вершины степени 2)
    G7 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (1, 2), (2, 3), (3, 0)})
    assert calculate_number_articul(G7) == 0, "Тест 7 (цикл) не пройден"

    # Тест 8: Сложный граф с несколькими точками сочленения
    G8 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0]),
        np.array([4.0]),
        np.array([5.0]),
        np.array([6.0])
    ], {(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 5), (5, 3), (3, 6)})
    assert calculate_number_articul(G8) == 2, "Тест 8 (сложный граф) не пройден"

    print("Все 8 тестов для calculate_number_articul прошли успешно!")


def test_calculate_number_triangle():
    # Тест 1: Граф с 3 вершинами без треугольников
    G1 = Graph([np.array([0.0]), np.array([1.0]), np.array([2.0])], {(0, 1), (1, 2)})
    assert calculate_number_triangle(G1) == 0, "Тест 1 (нет треугольников) не пройден"

    # Тест 2: Один треугольник
    G2 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0])
    ], {(0, 1), (1, 2), (2, 0)})
    assert calculate_number_triangle(G2) == 1, "Тест 2 (1 треугольник) не пройден"

    # Тест 3: Два раздельных треугольника
    G3 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0]),
        np.array([4.0]),
        np.array([5.0])
    ], {(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)})
    assert calculate_number_triangle(G3) == 2, "Тест 3 (2 треугольника) не пройден"

    # Тест 4: Треугольники с общей вершиной
    G4 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)})
    assert calculate_number_triangle(G4) == 2, "Тест 4 (2 треугольника с общей вершиной) не пройден"

    # Тест 5: Полный граф K4 (4 треугольника)
    G5 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)})
    assert calculate_number_triangle(G5) == 4, "Тест 5 (K4 - 4 треугольника) не пройден"

    # Тест 6: Граф с треугольником и дополнительными ребрами
    G6 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (1, 2), (2, 0), (0, 3), (1, 3)})
    assert calculate_number_triangle(G6) == 2, "Тест 6 (1 треугольник + доп. ребра) не пройден"

    # Тест 7: Граф без треугольников (дерево)
    G7 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0])
    ], {(0, 1), (0, 2), (0, 3)})
    assert calculate_number_triangle(G7) == 0, "Тест 7 (дерево) не пройден"

    # Тест 8: Сложный граф с 3 треугольниками
    G8 = Graph([
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([3.0]),
        np.array([4.0])
    ], {(0, 1), (1, 2), (2, 0), (0, 3), (3, 4), (4, 0), (1, 3)})
    assert calculate_number_triangle(G8) == 3, "Тест 8 (3 треугольника) не пройден"

    print("Все 8 тестов для calculate_number_triangle прошли успешно!")


def test_calculate_clique_number():
    # Тест 1: Одна вершина (тривиальная клика)
    G1 = Graph([1], {})
    assert calculate_clique_number(G1) == 1, "Тест 1 (1 вершина) не пройден"

    # Тест 2: Две несвязанные вершины
    G2 = Graph([1, 2], {})
    assert calculate_clique_number(G2) == 1, "Тест 2 (2 несвязанные вершины) не пройден"

    # Тест 3: Две связанные вершины (ребро)
    G3 = Graph([1,2], {(0, 1)})
    assert calculate_clique_number(G3) == 2, "Тест 3 (2 связанные вершины) не пройден"

    # Тест 4: Треугольник (3 вершины, все связаны)
    G4 = Graph([1, 2, 3], {(0, 1), (1, 2), (2, 0)})
    assert calculate_clique_number(G4) == 3, "Тест 4 (треугольник) не пройден"

    # Тест 5: Граф с кликой размера 4
    G5 = Graph([1, 2, 3, 4], {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)})
    assert calculate_clique_number(G5) == 4, "Тест 5 (клика K4) не пройден"

    # Тест 6: Граф с несколькими кликами разного размера
    G6 = Graph([1, 2, 3, 4], {(0, 1), (1, 2), (2, 3), (0, 2), (1, 3)})
    assert calculate_clique_number(G6) == 3, "Тест 6 (макс клика - треугольник) не пройден"

    # Тест 7: "Звезда" (1 центральная вершина, связанная с несколькими)
    G7 = Graph([1, 2, 3, 4, 5], {(0, 1), (0, 2), (0, 3), (0, 4)})
    assert calculate_clique_number(G7) == 2, "Тест 7 (звезда) не пройден"

    # Тест 8: Граф с изолированной вершиной и кликой
    G8 = Graph([1, 2, 3, 4, 5], {(0, 1), (1, 2), (2, 0), (3, 4)})
    assert calculate_clique_number(G8) == 3, "Тест 8 (клика + изолированные) не пройден"

    print("Все 8 тестов для calculate_clique_number прошли успешно!")


def test_calculate_maxsize_independed_set():
    # Тест 1: Одна вершина (тривиальное независимое множество)
    G1 = Graph([1])
    assert calculate_maxsize_independed_set(G1) == 1, "Тест 1 (1 вершина) не пройден"

    # Тест 2: Две несвязанные вершины
    G2 = Graph([1, 2], {})
    assert calculate_maxsize_independed_set(G2) == 2, "Тест 2 (2 несвязанные вершины) не пройден"

    # Тест 3: Две связанные вершины (ребро)
    G3 = Graph([1, 2], {(0, 1)})
    assert calculate_maxsize_independed_set(G3) == 1, "Тест 3 (2 связанные вершины) не пройден"

    # Тест 4: Треугольник (3 вершины, все связаны)
    G4 = Graph([1, 2, 3], {(0, 1), (1, 2), (2, 0)})
    assert calculate_maxsize_independed_set(G4) == 1, "Тест 4 (треугольник) не пройден"

    # Тест 5: Граф без треугольников (макс. независимое множество = 2)
    G5 = Graph([1, 2, 3, 4, 5], {(0, 1), (1, 2), (2, 3), (3, 4)})
    assert calculate_maxsize_independed_set(G5) == 3, "Тест 5 (цепочка) не пройден"

    # Тест 6: "Звезда" (1 центр + n вершин)
    G6 = Graph([1, 2, 3, 4, 5], {(0, 1), (0, 2), (0, 3), (0, 4)})
    assert calculate_maxsize_independed_set(G6) == 4, "Тест 6 (звезда) не пройден"

    # Тест 7: Решетка 2x2
    G7 = Graph([1, 2, 3, 4], {(0, 1), (1, 2), (2, 3), (3, 0)})
    assert calculate_maxsize_independed_set(G7) == 2, "Тест 7 (решетка) не пройден"

    # Тест 8: Граф с изолированной вершиной и кликой
    G8 = Graph([1, 2, 3, 4, 5], {(0, 1), (1, 2), (2, 0), (3, 4)})
    assert calculate_maxsize_independed_set(G8) == 2, "Тест 8 (клика + изолированные) не пройден"

    print("Все 8 тестов для calculate_maxsize_independed_set прошли успешно!")

if __name__ == "__main__":
    test_calculate_min_deg()
    test_calculate_max_deg()
    test_calculate_number_component()
    test_calculate_number_articul()
    test_calculate_number_triangle()
    test_calculate_clique_number()
    test_calculate_maxsize_independed_set()
