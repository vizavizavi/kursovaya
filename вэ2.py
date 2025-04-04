import numpy as np
import matplotlib.pyplot as plt

# Параметры
x = np.linspace(0, 1, 100)  # x от 0 до 1 м
IA = 0.002 * x**2  # IA в А, модель из графика (0 до 2 мА при x=1)
I0 = 0.00001 * np.ones_like(x)  # I0 постоянный, около 0.01 мА, через R3=1e6

# Перевод в мА для построения
IA_mA = IA * 1000
I0_mA = I0 * 1000

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(x, IA_mA, label='IA (мА)', color='blue')
plt.plot(x, I0_mA, label='I0 (мА)', color='red', linestyle='--')
plt.grid(True)
plt.xlabel('x (м)')
plt.ylabel('Ток (мА)')
plt.title('Зависимость тока от положения x')
plt.legend()
plt.show()