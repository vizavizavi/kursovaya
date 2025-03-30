def req(r, tolerance=1e-6):  
    R_prev = 0  
    R_curr = r  
    while abs(R_curr - R_prev) > tolerance:  
        R_prev = R_curr  
        R_curr = r + (2 * r * R_prev) / (2 * r + R_prev)  
    return R_curr  
print(req(10))  
