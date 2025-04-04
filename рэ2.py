from sympy import symbols, sqrt, pi, exp, I, simplify

# Определение символьных переменных
U_ll = symbols('U_ll')  # Линейное напряжение (между фазами)
Z_load = symbols('Z_load')  # Импеданс нагрузки на фазу
theta = symbols('theta')  # Угол нагрузки (если требуется)

# Углы фазовых сдвигов (120 градусов в радианах)
alpha = 2 * pi / 3

# Фазные напряжения для соединения "звезда" (U_phase = U_line / sqrt(3))
U_A = U_ll / sqrt(3) * exp(I * 0)
U_B = U_ll / sqrt(3) * exp(-I * alpha)
U_C = U_ll / sqrt(3) * exp(I * alpha)

# Токи в фазах (для симметричной нагрузки)
I_A = U_A / Z_load
I_B = U_B / Z_load
I_C = U_C / Z_load

# Для соединения "треугольник" (U_phase = U_line)
I_AB = U_ll / Z_load
I_BC = I_AB * exp(-I * alpha)
I_CA = I_AB * exp(I * alpha)

# Линейные токи через фазные (по первому закону Кирхгофа)
I_A_delta = I_AB - I_CA
I_B_delta = I_BC - I_AB
I_C_delta = I_CA - I_BC

# Упрощение выражений
I_A_delta = simplify(I_A_delta)
I_B_delta = simplify(I_B_delta)
I_C_delta = simplify(I_C_delta)

print("Токи при соединении ЗВЕЗДОЙ (Y):")
print(f"I_A = {I_A}")
print(f"I_B = {I_B}")
print(f"I_C = {I_C}\n")

print("Токи при соединении ТРЕУГОЛЬНИКОМ (Δ):")
print(f"I_A = {I_A_delta}")
print(f"I_B = {I_B_delta}")
print(f"I_C = {I_C_delta}")