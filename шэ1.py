def parallel_resistance(resistors):
    return 1 / sum(1 / r for r in resistors)

R1, R2, R3 = 2, 3, 6
R_eq = parallel_resistance([R1, R2, R3])
print(f"Эквивалентное сопротивление: {R_eq:.2f} Ом")
