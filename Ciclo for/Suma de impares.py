Valor = int(input("Cuantos numeros quieres:"))
Suma = 0
for num in range(1, Valor +1):
    res = num % 2
    if res == 1:
        Suma += num
print(Suma)