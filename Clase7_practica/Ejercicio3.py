#Luis Roberto Ardón y José David Franco

import random

n = int(input("Dime el numero de veces que tire el dado: "))
suma = 0

for i in range(1, n + 1):
    tiro = random.randint(1,6)
    print(f"Tirada {i}:", tiro)
    suma = suma + tiro

promedio = suma / n

print(f"Suma total:", suma)
print("Promedio:", promedio)
if promedio > 3.5:
    print("¡Buena racha!")
else: 
    print("¡Sigue intentando!")