Año = int(input("Dime el año que es:"))
m_actual = int(input("En que mes estamos (1-12):"))
Nacimiento = int(input("En que año Naciste:"))
mes = int(input("Mes de Nacimiento:"))
"""Operacion"""
Edad = Año - Nacimiento
if mes >= Nacimiento:
    print(f"Tu Cumplistes {Edad} años")
elif mes <= Nacimiento:
    print(f"Tu Cumpliras {Edad} años")