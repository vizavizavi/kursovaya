import math

R = 50
C = 100e-6
f = 50
X_C = 1 / (2 * math.pi * f * C)
Z = math.sqrt(R**2 + X_C**2)
print(f"Импеданс: {Z:.2f} Ом")

