#Luis Roberto Ardón - 20250081 y Santiago Cabarrus - 20250411

a = int(input("Ingresa el valor del lado a del triangulo: ")) #Asignamos una variable para que el usuario asigne un valor
b = int(input("Ingresa el valor del lado b del triangulo: ")) #Asignamos una variable para que el usuario asigne un valor
c = int(input("Ingresa el valor del lado c del triangulo: ")) #Asignamos una variable para que el usuario asigne un valor
if a == b and b == c:   #Condicion principal porque tiene que cumplir 3 parametros (3 lados iguales)
    print("El triangulo es equilatero")
elif a == b or b == c or a == c:  #condicion elif porque se tienen que cumplir 2 parametros (2 lados iguales)
    print("El triangulo es isoceles")
else:  #si ninguno se cumple
    print("El triangulo es escaleno")
print("Ahora sabes geometria :)")
