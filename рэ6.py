import numpy as np
import matplotlib.pyplot as plt

# Данные
E = 24  # ЭДС, В
Ra = 10  # Сопротивление реостата, Ом
Ia = 1.6  # Ток, А
Rb = 40  # Сопротивление реостата, Ом
Ib = 1.2  # Ток, А

# Система уравнений
# 0.8 R1 R2 - 4 R1 - 12 R2 - 120 = 0
# 0.6 R1 R2 + 12 R1 - 12 R2 - 480 = 0
# После упрощения: R2 = 5 R1 - 130
# Подстановка: R1^2 - 42 R1 + 360 = 0

# Решение квадратного уравнения для R1
a = 1
b = -42
c = 360
delta = b**2 - 4*a*c
R1_1 = (-b + np.sqrt(delta)) / (2*a)
R1_2 = (-b - np.sqrt(delta)) / (2*a)

# Находим R2
R2_1 = 5 * R1_1 - 130
R2_2 = 5 * R1_2 - 130

# Выбираем физически возможное решение
if R2_1 > 0:
    R1, R2 = R1_1, R2_1
else:
    R1, R2 = R1_2, R2_2

print(f"R1 = {R1:.2f} Ом")
print(f"R2 = {R2:.2f} Ом")

# Визуализация зависимости тока от Rx
Rx = np.linspace(0, 50, 100)
R_eq = (R1 * (R2 + Rx)) / (R1 + R2 + Rx)
I = E / R_eq

plt.figure(figsize=(10, 6))
plt.plot(Rx, I, label='Ток I (А)', color='blue')
plt.scatter([Ra, Rb], [Ia, Ib], color='red', label='Измеренные точки')
plt.grid(True)
plt.xlabel('Сопротивление реостата Rx (Ом)')
plt.ylabel('Ток I (А)')
plt.title('Зависимость тока от сопротивления реостата')
plt.legend()
plt.show()