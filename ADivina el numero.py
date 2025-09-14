Secreto = 25
for intentos in range(5):
   num = int(input("Cual es mi numero:"))
   if num == 25:
      print("Correcto, lo lograste")
      break
   elif num > 25:
        print("El numero es mas pequeño")
   elif num <25:
       print("El numero es mas grande")
else:
   print(f"Se acabaron los intentos. El numero secreto era: {Secreto}")

