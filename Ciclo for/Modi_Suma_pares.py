"""Modificacion para suma de numeros pares"""
Suma_Total = 0
for num in range (1,101):
    res = num % 2
    if res == 0:
        Suma_Total =  Suma_Total + num
print(f"la suma total es: {Suma_Total}")