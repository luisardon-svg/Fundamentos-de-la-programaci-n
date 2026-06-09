#Luis Roberto Ardón - 20250081 y Mariana Duarte - 20250049

rol = int(input("¿Cual es tu rol? (admin, usuario,) (1 para admin, 0 para usuario)")) # Pregunta el rol al usuario
print("Hola, si eres admin, bienvenido", administrador) #Si su rol es admin, puede entrar; de lo  contrario, no

edad = int(input("¿Cuantos años tienes?")) # Le pedimos su edad al usuario
contrasena = int(input("¿Cual es tu contrasena?")) #Luego, le pedimos su contraseña
puede_entrar = (edad >=18 and contrasena == 1234) or rol == 1 # Si la edad y contraseña son correctas, puede entrar; de lo contrario no

print("Hola, si eres admin o tienes la contrasena correcta y eres mayor de edad, bienvenido", puede_entrar)