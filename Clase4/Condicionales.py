#sistema de acceso para una persona.
#si tiene entre 15 y 17 anios puede ingresar con un adulto.
# si es mayor de 18 años, puede ingresar.
edad = int(input("Ingresa porfa tu edad: ")) #esto es una variable con un int input para que el usuario ingrese su edad.
nombre = input("¿Como te llamas? ")

if edad >=18: #si la edad es mayor o igual a 18, puede ingresar.
    print("Hola", nombre + ",", "puedes entrar al establecimiento") #esto se va a ejecutar media vez la pesrona sea mayor de 18 anios.
elif edad >=15 and edad < 18: # esto es una condicional elif para que la persona pueda entrar con sus papas o con un adulto.
    print("Hola :)", nombre + ",", "puedes entrar al establecimiento PERO acompañado de un adulto") #esto se va a ejecutar media vez la persona tenga entre 15 y 17 anios.
else: 
    print("Hola:)", nombre + ",", "Lo lamento mucho, no puedes entrar")