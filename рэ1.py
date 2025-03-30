E = 36
r = 2
R1 = 4
R2 = 3
R_dv = 6
eta_dv = 0.9
R_p = R1 * R_dv / (R1 + R_dv)
R_total = r + R2 + R_p
I = E / R_total
U_p = I * R_p
I_dv = U_p / R_dv
P_el = U_p * I_dv
P_pol = eta_dv * P_el
P_ist = E * I
eta = P_pol / P_ist
print(f"КПД с R1: {eta:.2f}")

R_total_no_R1 = r + R2 + R_dv
I_no_R1 = E / R_total_no_R1
P_pol_no_R1 = eta_dv * (I_no_R1**2 * R_dv)
eta_no_R1 = P_pol_no_R1 / (E * I_no_R1)
print(f"КПД без R1: {eta_no_R1:.2f}")
