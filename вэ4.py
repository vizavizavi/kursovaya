import numpy as np
import matplotlib.pyplot as plt

# Параметры
n_vertices = 2017  # Количество вершин (2017-угольник)
U0 = 1  # Напряжение U0 (принимаем 1 для упрощения, так как это множитель)
N = np.arange(1, n_vertices + 1)  # Номера вершин от 1 до 2017
voltages = (N - 1) * U0  # Показания вольтметров V_N = (N-1)U0

# 1) Разница между показаниями первого и десятого вольтметров
V1 = voltages[0]  # Показания V_1 (N=1)
V10 = voltages[9]  # Показания V_10 (N=10)
difference = V10 - V1
print(f"Разница между показаниями V_1 и V_10: {difference} U_0")

# 2) Показания вольтметра с номером N (формула уже определена как (N-1)U_0)
# Пример для N=10
N_example = 10
V_N_example = voltages[N_example - 1]
print(f"Показания вольтметра V_{N_example}: {V_N_example} U_0")

# 3) Номер вольтметра с нулевыми показаниями
zero_reading_index = np.where(voltages == 0)[0][0] + 1  # +1, так как индексы начинаются с 0
print(f"Номер вольтметра с нулевыми показаниями: {zero_reading_index}")

# Визуализация
plt.figure(figsize=(10, 6))
plt.plot(N, voltages, label='Показания вольтметров (в единицах U_0)', color='blue')
plt.grid(True)
plt.xlabel('Номер вольтметра N')
plt.ylabel('Показания (в единицах U_0)')
plt.title('Зависимость показаний вольтметров от номера N')
plt.legend()
plt.show()