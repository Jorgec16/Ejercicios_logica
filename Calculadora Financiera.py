"""capital inicial
tasa de interes
numero de periodos
resultado final monto final de inversion"""
print ("Quieres saber cuanto puedes ganar en tu inversion")
cap_ini= float(input ("Cual es tu monto inicial:") )
Tas_In= int(input("De cuanto es tu interes:"))
Num_Per = int(input("Por que periodo es:"))
"""Operacion"""
interes= Tas_In/100
print(interes)
Cal= cap_ini * (1+(interes))**Num_Per
print(f"El monto final de tu inversion es: {Cal}")