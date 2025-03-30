def star_to_delta(Ra, Rb, Rc):
    R12 = (Ra * Rb + Ra * Rc + Rb * Rc) / Rc
    R13 = (Ra * Rb + Ra * Rc + Rb * Rc) / Rb
    R23 = (Ra * Rb + Ra * Rc + Rb * Rc) / Ra
    return R12, R13, R23

Ra, Rb, Rc = 1, 1, 1
R12, R13, R23 = star_to_delta(Ra, Rb, Rc)
print(f"R12 = {R12:.2f}, R13 = {R13:.2f}, R23 = {R23:.2f} Ом")
