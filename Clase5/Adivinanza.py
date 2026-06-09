print("Bienvenido al juego de adivinanza")
print("Intenta advinar el número que estoy pensando (entre 1 y 5)")

import random

adivinador = random.randint(1,5) #Generar un numero aleatorio entre 1 y 
usuario = int(input("Ingresa el numero que piensas que elegí: "))
if usuario == adivinador:
    print("Felicidades, advinaste mi numero secreto")
elif usuario > adivinador:
    print("Te pasaste mi hermano, el numero es más pequeño")
elif usuario < adivinador:
    print("Uy manito, te quedaste corto, el numero es más grande")
    
print("El numero que elegí era: ", adivinador)
