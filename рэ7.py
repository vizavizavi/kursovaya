import numpy as np
import matplotlib.pyplot as plt

# Параметры
U = 81  # Напряжение, В
R1 = 3  # кОм
R2 = 9  # кОм
R3 = 6  # кОм

# Диапазон R_x
Rx = np.linspace(0.01, 50, 1000)  # кОм

# Ток I_0
I0 = 9 * (18 + Rx) / (9 + Rx)  # мА

# Ток I через A1
I = 81 * np.abs(18 - Rx) / (3000 * (9 + Rx)) * 1000  # мА

# 1) Минимальная сила тока |I|
min_I = 0  # при R_x = 18 кОм
Rx_min_I = 18
print(f"Минимальная сила тока |I|: {min_I} мА при R_x = {Rx_min_I} кОм")

# 2) Максимальная сила тока |I|
max_I = 27  # при R_x = 0
Rx_max_I = 0
print(f"Максимальная сила тока |I|: {max_I} мА при R_x = {Rx_max_I} кОм")

# 3) I_0 = 1/2 |I|_max
I0_target = 0.5 * max_I  # 13.5 мА
Rx_I0_target = 9  # кОм
print(f"I_0 = {I0_target} мА при R_x = {Rx_I0_target} кОм")

# Визуализация
plt.figure(figsize=(10, 6))
plt.plot(Rx, np.abs(I), label='|I| (мА)', color='blue')
plt.plot(Rx, I0, label='I_0 (мА)', color='red')
plt.grid(True)
plt.xlabel('R_x (кОм)')
plt.ylabel('Ток (мА)')
plt.title('Зависимость токов от R_x')
plt.legend()
plt.show()