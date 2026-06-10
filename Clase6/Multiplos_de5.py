#Multiplos de 5

#Camino A:

for i in range(0, 51, 5):
    print(i)

#Camino B

print("Multiplos de 5 del 0 al 50")

numero = int(input("Ingresa un numero multiplo de 5: "))

if numero % 5 == 0:
    for i in range(numero, 51, 5):  #La i si es una variable
        print(i)
else: 
    print("El numero ingresado no es multiplo de 5")

#Otra forma:

for i in range(1, 51):
    if i % 5 == 0:
        print(i)
