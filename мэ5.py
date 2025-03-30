import math
import matplotlib.pyplot as plt

R = 30
L = 0.2
C = 50e-6
f = 60
U = 120
X_L = 2 * math.pi * f * L
X_C = 1 / (2 * math.pi * f * C)
Z = math.sqrt(R**2 + (X_L - X_C)**2)
I = U / Z
U_R = I * R
U_L = I * X_L
U_C = I * X_C
print(f"Ток: {I:.2f} А")

plt.quiver(0, 0, U_R, 0, angles='xy', scale_units='xy', scale=1, color='r', label='U_R')
plt.quiver(U_R, 0, 0, U_L, angles='xy', scale_units='xy', scale=1, color='g', label='U_L')
plt.quiver(U_R, 0, 0, -U_C, angles='xy', scale_units='xy', scale=1, color='b', label='U_C')
U_x = U_R
U_y = U_L - U_C
plt.quiver(0, 0, U_x, U_y, angles='xy', scale_units='xy', scale=1, color='k', label='U')
plt.xlim(-100, 150)
plt.ylim(-100, 150)
plt.legend()
plt.grid()
plt.show()
