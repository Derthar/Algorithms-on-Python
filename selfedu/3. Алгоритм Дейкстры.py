"""
Ищет самые короткие пути между начальной вершиной графа ко всем остальным вершинам с положительными дугами
Используется в маршрутизации, где вершины графов - серверы,а вес дуг - задержка сервера

1. Для начала составляется матрица смежности (где первый столбец и первая строка - вершины графа, а значения таблицы -
вес дуги между ними, или 0 - если прямой связи между вершинами нет)
"""
import math


# Функция возвращает все связанные вершины с вершиной v
def get_link_v(v, D):
     return [i for i, weight in enumerate(D[v]) if weight > 0]
     # for i, weight in enumerate(D[v]):
     #      if weight > 0:
     #           yield i


# Выбирает минимальное значение(после каждой итерации основного циклА) для вершин, которые еще не были полносью рассмотрены
# Или возвращает -1 если таких вершин нет
def arg_min(T, S):
     amin = -1
     m = max(T)  #
     for i, t in enumerate(T):
          if t < m and i not in S:
               m = t
               amin = i

     return amin


# Создаем матрицу смежности
D = ((8, 3, 1, 3, 0, 0),
     (3, 0, 4, 0, 0, 0),
     (1, 4, 0, 0, 7, 5),
     (3, 0, 0, 0, 0, 2),
     (0, 0, 7, 0, 0, 4),
     (0, 0, 5, 2, 4, 0)
    )

N = len(D)  # Число вершин в графе
T = [math.inf]*N  # Последняя строка таблицы( список из 8 "бесконечностей")

v = 0  #Стартовая вершина(нулевая)
S = {v}  # Просмотренные вершины
T[v] = 0  # Нулевой вес для стартовой вершины

while v != -1:  # Цикл пока не просмотрим все вершины
     for j in get_link_v(v, D):
          if j not in S:  # Если вершина еще не просмотрена то
               w = T[v] + D[v][j]  # Суммирует вес предыдущей вершины и вес до следуюей вершины
               if w < T[j]:  # Если вес оказался меньше предыдущего, то меняет значение
                    T[j] = w

     v = arg_min(T, S)  # возвращает вершину с минимальным весом, которая еще не была рассмотрена( или -1 если таких нет)
     if v > 0:
          S.add(v)

print(T)

















