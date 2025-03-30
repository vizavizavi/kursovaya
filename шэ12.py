U = 24
R1, R2, R3 = 2, 4, 6
R_p = R2 * R3 / (R2 + R3)
R_total = R1 + R_p
I_total = U / R_total
U_p = I_total * R_p
I2 = U_p / R2
I3 = U_p / R3
print(f"I через 2 Ом = {I_total:.2f} А, I через 4 Ом = {I2:.2f} А, I через 6 Ом = {I3:.2f} А")
