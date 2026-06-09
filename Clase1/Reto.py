#Luis Roberto Ardón - 20250081 y Mariana Duarte - 20250049
rol = int(input("¿Cual es tu rol? (admin, usuario,) (1 para admin, 0 para usuario)")) #Luego, le pedimos su rol
administrador = rol == 1
print("Hola, si eres admin, bienvenido", administrador) #Si el rol es admin, entonces puede administrar, de lo contrario no puede administrar

edad = int(input("¿Cuantos años tienes?")) #Primero le pedimos al usuario que ingrese su edad
contrasena = int(input("¿Cual es tu contrasena?")) #Luego, le pedimos su contraseña
puede_entrar = (edad >=18 and contrasena == 1234) or rol == 1

print("Hola, si eres admin o tienes la contrasena correcta y eres mayor de edad, bienvenido", puede_entrar)