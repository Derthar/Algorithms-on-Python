"""
В отличии от алгоритма Дейкстры работает с отрицательными весамиб и ищет кратчайшие пути сразу между всеми вершинами

1 Этап.
Составление матрицы смежности

2. Этап
Сравнение прямого пути между каждой парой вершини сравнение пути через каждую промежуточную вершину
Есл прямого пути нет то по умолчанию путь = бесконечность

Количестве вычислений = V**3

# Данная реализация несовершенна с точки зрения маршрута, но кратчайший суммарный путь вроде считает правильно
"""
import math

def get_path(L,start, end):
    path = [end]
    while end != start:
        end = L[end][start]
        path.append(end)

    return path[::-1]





c = math.inf


D = [
    [0, 2, c, 3, 1, c, c, 10],
    [2, 0, 4, c, c, c, c, c],
    [c, 4, 0, c, c, c, c, 3],
    [3, c, c, 0, c, c, c, 8],
    [1, c, c, c, 0, 2, c, c],
    [c, c, c, c, 2, 0, 3, c],
    [c, c, c, c, c, 3, 0, 1],
    [10, c, 3, 8, c, c, 1, 0]
]
for string in D:
    print(string)

lend = len(D)

P =  [[N for N in range(lend)] for u in range(lend)]


for n in range(lend):
    for i in range(lend):
        for j in range(lend):
             if D[i][j] > D[i][n]+D[n][j]:
                D[i][j] = D[i][n]+D[n][j]
                P[i][j] = n

print('*************************')
for string in D:
    print(string)
print('*************************')
for string in P:
    print(string)

print('*************************')
print(get_path(P, 2, 4))
print(D[2][4])


# import math
#
#
# def get_path(P, u, v):
#     path = [u]
#     while u != v:
#         u = P[u][v]
#         path.append(u)
#
#     return path[::-1]
#
#
# V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
#      [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
#      [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
#      [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
#      [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
#      [10, math.inf, 3, 8, math.inf, math.inf, 1, 0],
# ]
#
# N = len(V)                       # число вершин в графе
# P = [[v for v in range(N)] for u in range(N)]       # начальный список предыдущих вершин для поиска кратчайших маршрутов
#
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             d = V[i][k] + V[k][j]
#             if V[i][j] > d:
#                 V[i][j] = d
#                 P[i][j] = k     # номер промежуточной вершины при движении от i к j
#
# # нумерацця вершин начинается с нуля
# start = 2
# end = 4
# print(V[start][end])
# print(get_path(P, end, start))








