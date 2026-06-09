print("Bienvenido al juego del adivinador, el juego consiste en adivinar el numero secreto, si lo advinas perfecto, sino MUERES")
secreto = 67 #Asignamos el numero secreto a una variable
intento = int(input("Adivina el numero secreto (es un numero entero): ")) #Asignamos la variable para que el usuario ingrese su intento
if intento == secreto: #Si el intento es igual al numero secreto, el usuario gana
    print("¡Felicidades, adivinaste mi numero secreto, te ganaste un premio ;)")
elif intento > secreto: #Si el intento es mayor al numero secreto, le decimos que se paso y le damos una pista
    print("¡Uy mano te pasaste un talego men, intenta con un numero mas pequeño")
    print("Te doy una pista, la diferencia de tu numero con el numero secreto es ", abs(intento - secreto))
elif intento < secreto: #Si el intento es menor al numero secreto, le decimos que se quedo corto y le damos una pista
    print("Como asi broder, te quedaste corto men, intenta con un numero mas grande")
    print("Te doy una pista, la diferencia de tu numero con el numero secreto es ", abs(intento - secreto))
print("Tu intento: ", intento)