I1 = 0.2  
I2 = I1 / 3
print(f"Показания амперметра A2: {I2:.4f} мА")
I_upper = 2 * I2
print(f"Ток через верхнюю ветвь: {I_upper:.4f} мА")
I_total = I_upper + I2
print(f"Проверка, общий ток: {I_total:.4f} мА (должен быть равен {I1} мА)")