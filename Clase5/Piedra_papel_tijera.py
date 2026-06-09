from random import choice
#Jugada del usuario:
usuario = input("Elige piedra, papel o tijera: ")

#Jugada de la computadora:

pc = choice(["piedra", "papel", "tijera"])
print("La computadora eligió: ", pc)

if usuario == "piedra" and pc == "tijera":
    print("¡Ganaste!")
elif usuario == "papel" and pc == "piedra":
    print("¡Ganaste!")
elif usuario == "tijera" and pc == "papel":
    print("¡Ganaste!")
elif usuario == pc:
    print("¡Empate!")

else:
    print("Perdiste.")
