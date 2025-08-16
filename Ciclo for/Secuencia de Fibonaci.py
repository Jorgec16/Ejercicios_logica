Total = int(input("Cuantos numero quieres que imprima:"))
num1 = 0
num2 = 1
for num in range(Total):
    if num == 0:
        print(num1)
    elif num == 1:
        print(num2)
    else:
        Suma = num1 + num2
        print(Suma)
        """Actualizamos los valores"""
        num1 = num2
        num2 = Suma
    
    