import numpy as np
import matplotlib.pyplot as plt

R = 10
L = 0.1
C = 100e-6
f = np.linspace(1, 1000, 1000)  # Начинаем с 1 Гц, чтобы избежать деления на 0
X_L = 2 * np.pi * f * L
X_C = 1 / (2 * np.pi * f * C)
Z = np.sqrt(R**2 + (X_L - X_C)**2)
plt.plot(f, Z)
plt.xlabel('Частота (Гц)')
plt.ylabel('Импеданс (Ом)')
plt.grid()
plt.show()

