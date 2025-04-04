import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def compute_equivalent_resistance_cube_3x3x3(R=1.0):
    # Размер куба: 3x3x3
    n = 3
    num_nodes = n * n * n  # 27 узлов

    # Матрица проводимостей
    G = np.zeros((num_nodes, num_nodes))
    # Вектор токов
    I = np.zeros(num_nodes)

    # Нумерация узлов: (i,j,k) -> i*n*n + j*n + k
    def node_index(i, j, k):
        return i * n * n + j * n + k

    # Заполняем матрицу проводимостей
    for i in range(n):
        for j in range(n):
            for k in range(n):
                node = node_index(i, j, k)
                # Соседи узла
                neighbors = []
                # По оси x
                if i > 0:
                    neighbors.append(node_index(i-1, j, k))
                if i < n-1:
                    neighbors.append(node_index(i+1, j, k))
                # По оси y
                if j > 0:
                    neighbors.append(node_index(i, j-1, k))
                if j < n-1:
                    neighbors.append(node_index(i, j+1, k))
                # По оси z
                if k > 0:
                    neighbors.append(node_index(i, j, k-1))
                if k < n-1:
                    neighbors.append(node_index(i, j, k+1))

                # Проводимость 1/R между узлом и соседями
                for neighbor in neighbors:
                    G[node, neighbor] = -1/R
                    G[node, node] += 1/R

    # Вводим ток I в узел (0,0,0) и выводим из (2,2,2)
    node1 = node_index(0, 0, 0)  # (0,0,0)
    node2 = node_index(2, 2, 2)  # (2,2,2)
    I[node1] = 1  # Ток 1 А входит
    I[node2] = -1  # Ток 1 А выходит

    # Решаем систему G * V = I для потенциалов V
    V = la.solve(G, I)

    # Разность потенциалов между узлами
    delta_V = V[node1] - V[node2]

    # Эквивалентное сопротивление R_eq = delta_V / I, I = 1
    R_eq = delta_V
    return R_eq

# Вычисляем R_eq для куба 3x3x3
R = 1.0  # Сопротивление каждого резистора
R_eq = compute_equivalent_resistance_cube_3x3x3(R)
print(f"Численное R_eq = {R_eq:.4f} R")

# Теоретическое значение
R_eq_theoretical = (5/6) * R
print(f"Теоретическое R_eq = {R_eq_theoretical:.4f} R")

# Проверка для разных размеров куба (2x2x2 и 3x3x3 для сравнения)
def compute_for_size(n, R=1.0):
    num_nodes = n * n * n
    G = np.zeros((num_nodes, num_nodes))
    I = np.zeros(num_nodes)

    def node_index(i, j, k):
        return i * n * n + j * n + k

    for i in range(n):
        for j in range(n):
            for k in range(n):
                node = node_index(i, j, k)
                neighbors = []
                if i > 0:
                    neighbors.append(node_index(i-1, j, k))
                if i < n-1:
                    neighbors.append(node_index(i+1, j, k))
                if j > 0:
                    neighbors.append(node_index(i, j-1, k))
                if j < n-1:
                    neighbors.append(node_index(i, j+1, k))
                if k > 0:
                    neighbors.append(node_index(i, j, k-1))
                if k < n-1:
                    neighbors.append(node_index(i, j, k+1))

                for neighbor in neighbors:
                    G[node, neighbor] = -1/R
                    G[node, node] += 1/R

    node1 = node_index(0, 0, 0)
    node2 = node_index(n-1, n-1, n-1)
    I[node1] = 1
    I[node2] = -1

    V = la.solve(G, I)
    delta_V = V[node1] - V[node2]
    return delta_V

# Сравнение для n=2 и n=3
sizes = [2, 3]
R_eq_values = [compute_for_size(n) for n in sizes]

# Визуализация
plt.figure(figsize=(10, 6))
plt.plot(sizes, R_eq_values, marker='o', label='Численное R_eq')
plt.axhline(y=R_eq_theoretical, color='r', linestyle='--', label='Теоретическое R_eq = 5/6 R')
plt.grid(True)
plt.xlabel('Размер куба n (n x n x n)')
plt.ylabel('Эквивалентное сопротивление (в единицах R)')
plt.title('Эквивалентное сопротивление куба из резисторов')
plt.legend()
plt.show()