#Luis Roberto Ardón - 20250081 y Mariana Duarte - 20250049

nombre = str(input("¿Como te llamas?")) #Le pedimos su nombre
edad = int(input("¿Cuantos años tienes?")) #Le pedimos su edad
es_adulto = edad >= 18 #Preguntamos si es mayor de edad
anio = 2026 - edad #Calculamos el año de nacimiento
print("Hola", nombre, "naciste en", anio, "y", "eres adulto:", es_adulto) #Si es mayor de edad, puede entrar; de lo contrario, no