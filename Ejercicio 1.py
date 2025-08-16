"""Operadores"""
#Aritmeticos
sum = 10 + 5
print(sum)
print(2+4 , "Suma")
print(f"Suma: 10 + 3 = {10 +3}")
print(2-4, "Resta") 
print(2*4 , "Multiplicacion")
print(10/2 , "Division")
print(f"Modulo: 10 % 2 = {10 % 5}")
print(f"Exponencial: 10**3 = {10**3}")
print(f"Division entera: 10//3 ={10//3}")
#Operadores de comparacion
print(f"Igualdad: 10 == 3 es {10==3}")
print(f"Desigualdad 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3: {10 > 3}")
print(f"Menor que: 10 < 3: {10 < 3}")
print(f"Mayor o igual que: 10 >= 10: {10 >= 10}")
print(f"Menor o igual que: 10 <= 3: {10 <= 3}")

#Operadores logicos
print(f"And &&: 10 + 3 == 13 and 5-1 == 4 es {10 +3 == 13 and 5-1 == 4}") #ambas condiciones sea verdadera
print(f"Or ||: 10 + 3 == 14 or 5-1 == 4 es {10 +4 == 14 or 5-1 == 4}") #sea verdadera por lo menos una condicion
print(f"Not !: not 10 + 3 == 14 es {not 10 +3 == 14}")

#Operadores de asiganacion
my_number = 11
print(my_number)
my_number += 1 #suma y asignacion
print(my_number)
my_number -= 1 #resta y asignacion
print(my_number)
my_number *= 2 #Multiplicacion y asignacion
print(my_number)
my_number /= 2 #division y asignacion
print(my_number)
my_number %= 2 #Modulo y asignacion
print(my_number)
my_number **= 1 #exponente y asignacion
print(my_number)
my_number //= 1 #division entera y asignacion
print(my_number)

#Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")#igualdad sirven para comparar dos objetos
print(f"my_number is not my_new_number es {my_number is not my_new_number}") #desigualdad 

#Operador de pertenecia
print(f"o in jorge = {"o" in "jorge"}")# es para comprobar si algo existe en otro objeto o componenete
print(f"b in jorge = {"b" in "jorge"}")

#Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"And 10 & 3 = {10 & 3}")
print(f"Or 10 | 3 = {10 | 3}")
print(f"Xor 10 ^ 3 = {10 ^ 3}")
print(f"Not 10 ~ 3 = {~10}")
print(f"Desplazamiento a la derecha 10>>2 = {10 >> 2}")
print(f"Desplazamiento a la izquierda 10<<2 = {10 << 2}")

"""Estructuras de control"""

#Condicionales

my_string = "Jorge"

if my_string == "Jorge":
    print("Hola" + my_string)
elif my_string == "Campuzano":
    print("Mi apellido es:" + my_string)
else:
    print("Adios")

# Interativas
for i in range (11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("No ha finalizado el manejo de excepciones")

#Extra
for n1 in range(10 , 56):
    if n1 %2 == 0 and n1 != 16 and n1 %3 == 0:
        print(n1)