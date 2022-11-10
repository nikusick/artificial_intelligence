"""Найти длину гамильтонова цикла S4 в полном графе K6 после четырех
циклов решения задачи методом отжига."""

import networkx as nx
from math import e

distances = [
    (1, 2, 26), (1, 3, 42), (1, 4, 44), (1, 5, 31), (1, 6, 31),
    (2, 3, 20), (2, 4, 34), (2, 5, 40), (2, 6, 15), (3, 4, 23),
    (3, 5, 43), (3, 6, 20), (4, 5, 27), (4, 6, 22), (5, 6, 26)
]

V = [1, 2, 3, 4, 5, 6, 1]
P = [90, 45, 43, 31]
Z = [(3, 4), (4, 6), (5, 6), (6, 2)]
T = 100


def probability(delta, T):
    return 100 * e ** (-delta / T)


def reduct_temp(prev_t):
    next_t = 0.5 * prev_t
    return next_t


graph = nx.Graph()
graph.add_weighted_edges_from(distances)

nx.draw_kamada_kawai(graph, node_color='red', node_size=2000, with_labels=True)


def edge_length(i, j, distances, round_trip=True):
    if round_trip:
        return max([item[2] if (item[0] == i and item[1] == j)
                               or (item[1] == i and item[0] == j) else -1
                    for item in distances])
    else:
        return max([item[2] if (item[0] == i and item[1] == j) else -1
                    for item in distances])


def route_length(V, distances):
    edges = []
    for i in range(len(V) - 1):
        edges.append(edge_length(V[i], V[i + 1], distances))

    return sum(edges)


def route_one_replacement(arr_v, z, replace_by_name=True):
    decrement = 1 if replace_by_name else 0

    arr_v[z[0] - decrement], arr_v[z[1] - decrement] = arr_v[z[1] - decrement], arr_v[z[0] - decrement]
    return arr_v


def route_replacement(V, z):
    for _z in z:
        V = route_one_replacement(V, _z)
    return V


def choose_route(distances, v, z, t, p):
    sum_length = route_length(v, distances)
    arr_sum = [sum_length]

    for i in range(len(z)):
        new_v = route_one_replacement(v[:], z[i])
        new_s = route_length(new_v, distances)
        arr_sum.append(new_s)
        delta_s = new_s - sum_length

        if delta_s > 0:
            _p = probability(delta_s, t)
            if _p > p[i]:
                v = new_v
                sum_length = new_s
        else:
            v = new_v
            sum_length = new_s

        t = reduct_temp(t)

    return v, arr_sum


best_route, arr_length = choose_route(distances, V, Z, T, P)

print(f'Лучший маршрут: {best_route}')
print(f'Его длина: {route_length(best_route, distances)}')
print(f'Длины всех рассмотренных маршрутов: {arr_length}')

