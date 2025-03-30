R = 160
U = 220
t = 1200
m = 0.5
T0 = 20
c = 4200
L = 2.26e6
P = U**2 / R
Q = P * t
Q_nagrev = m * c * (100 - T0)
Q_isp = Q - Q_nagrev
m1 = Q_isp / L
print(f"Масса выкипевшей воды: {m1*1000:.1f} г")
