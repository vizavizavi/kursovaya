import numpy as np
import matplotlib.pyplot as plt

# Параметры
R1 = 5  # Сопротивление резистора, Ом
R0 = 20  # Полное сопротивление реостата, Ом
x = np.linspace(0.01, 19.99, 1000)  # Положение движка (избегаем деления на 0)

# Эквивалентное сопротивление
R_eq = x + (R1 * (R0 - x)) / (R1 + (R0 - x))

# Нахождение максимума
max_R_eq = np.max(R_eq)
max_x = x[np.argmax(R_eq)]

print(f"Максимальное показание омметра: {max_R_eq:.2f} Ом")
print(f"Положение движка x при максимуме: {max_x:.2f} Ом")

# Визуализация
plt.figure(figsize=(10, 6))
plt.plot(x, R_eq, label='Эквивалентное сопротивление (Ом)', color='blue')
plt.grid(True)
plt.xlabel('Сопротивление x (Ом)')
plt.ylabel('Эквивалентное сопротивление (Ом)')
plt.title('Зависимость эквивалентного сопротивления от положения движка')
plt.legend()
plt.show()