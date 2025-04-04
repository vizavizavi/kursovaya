from scipy.optimize import newton  
I0 = 1e-12  
Vt = 0.026  
def diode_current(V):  
    return I0 * (np.exp(V / Vt) - 1) - I  
I = 0.001  
V_solution = newton(lambda V: diode_current(V), 0.6)  
print(V_solution)  
