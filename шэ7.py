
U0 = 10.0  
n = 3     

# 1. Последовательное подключение
voltage_series = U0 / n
print(f"Напряжение на каждом вольтметре при последовательном подключении: {voltage_series:.3f} В")

# 2. Параллельное подключение
voltage_parallel = U0
print(f"Напряжение на каждом вольтметре при параллельном подключении: {voltage_parallel:.3f} В")