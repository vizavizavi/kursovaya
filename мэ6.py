import numpy as np

r = 90  
U0 = 5  
V_A = U0  
V_C = 0   
A = np.array([[3, -1], [-1, 3]])  
b = np.array([5, 5])              
V_B, V_O = np.linalg.solve(A, b)
I_AB = (V_A - V_B) / r  
I_AO = (V_A - V_O) / r  
I_AC = (V_A - V_C) / r  
I_total = I_AB + I_AO + I_AC  

I_total_mA = round(I_total * 1000)

V_BC = V_B - V_C
V_BC_rounded = round(V_BC)

V_AC = V_A - V_C
V_AC_rounded = round(V_AC)

print(f"1. Сила тока через батарейку: {I_total_mA} мА")
print(f"2. Напряжение между B и C: {V_BC_rounded} В")
print(f"3. Напряжение между A и C: {V_AC_rounded} В")

