palabra = input("Cual es tu palabra:")
Vocales = 0
for le in palabra:
    if le in "aeiou":
        Vocales = Vocales + 1
print(F"la cantidad de vocales es: {Vocales}")