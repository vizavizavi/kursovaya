import numpy as np
import matplotlib.pyplot as plt

R_values = np.linspace(1, 20, 100)
U0 = 24
I = U0 / R_values

plt.figure(figsize=(10, 6))
plt.plot(R_values, I*1000, label='Current I (mA)', color='blue')
plt.grid(True)
plt.xlabel('Resistance R (Ω)')
plt.ylabel('Current (mA)')
plt.title('Current vs Resistance in Tetrahedral Circuit')
plt.legend()
plt.show()
