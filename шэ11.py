U = 3000
I_dv = 190
n_dv = 8
F = 343e3
v = 42 / 3.6
I_total = n_dv * I_dv
P = U * I_total / 1e6
N = F * v / 1e6
eta = N / P
print(f"P = {P:.2f} МВт, N = {N:.2f} МВт, eta = {eta:.2f}")
