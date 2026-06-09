#Luis Roberto Ardón - 20250081 y Santiago Cabarrus - 2025

a = int(input("Ingresa el valor del lado a del triangulo: "))
b = int(input("Ingresa el valor del lado b del triangulo: "))
c = int(input("Ingresa el valor del lado c del triangulo: "))
if a == b and b == c:
    print("El triangulo es equilatero")
elif a == b or b == c or a == c:
    print("El triangulo es isoceles")
else:
    print("El triangulo es escaleno")
print("Ahora sabes geometria :)")
