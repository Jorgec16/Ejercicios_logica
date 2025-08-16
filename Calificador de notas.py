Nota = int(input("Cual es tu Nota:"))
if Nota >= 90 and Nota <= 100:
    print("Sobresaliente")
elif Nota >= 80 and Nota <= 89:
    print("Notable")
elif Nota >= 70 and Nota <= 79:
    print("Aprobado")
elif Nota >= 0 and Nota <= 69:
    print("Reprobado")
else:
    print("Calificación no válida")
