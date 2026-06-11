#Luis Roberto Ardón y José David Franco

numero = int(input("Ingrese un número: "))

for i in range(1, 11):
    total = numero * i

    if total % 2 == 0:     
        print(numero, "*", i, "=", total, "<- es par")
    else:
        print(numero, "*", i, "=", total )



