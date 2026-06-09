#Luis Roberto Ardón - 20250081 y Mariana Duarte - 20250049

nombre = str(input("¿Como te llamas?")) #Primero le pedimos al usuario que ingrese su nombre
edad = int(input("¿Cuantos años tienes?")) #Luego, le pedimos sus edad
boleto = int(input("¿Tienes boleto? (1 para si, 0 para no)")) #Asignamos la variable boleto, que si sí tiene marque 1, y si no marque 2
puede_entrar = edad >=18 and boleto == 1 #Aqui preguntamos si el usuario tiene boleto, y si marcó 1 y es mayor de dad puede entrar. De lo contrario, es falso

print("Hola", nombre, "si tienes boleto y eres mayor de edad, bienvenido", puede_entrar)