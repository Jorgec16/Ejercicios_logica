#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
Edad = int(input("Cual es tu edad:"))
if Edad >= 18:
    print("Es mayor de edad")
else:
    print(" Es menor de edad")


"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
 Si el divisor es cero el programa debe mostrar un error."""
numero_1= int(input("Cual es tu numero 1:"))
numero_2= int(input("Cual es el numero2:"))
if numero_2 == 0:
    print("Error")
else:
    print(numero_1/numero_2)

"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por 
el usuario coincide con la guardada en la
 variable sin tener en cuenta mayúsculas y minúsculas."""

Contraseña = input("Cual es tu contaseña")
if Contraseña == "Hola":
    print("Ingresaste")
else:
    print("Error")