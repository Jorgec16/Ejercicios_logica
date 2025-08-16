Precio = int(input("Cual es el Precio:"))
P_des = int(input("Cual es el descuento:"))
"""Operación"""
descuento = Precio * P_des / 100
P_final = Precio - descuento
print(f"El Precio final a pagar es: {P_final}")