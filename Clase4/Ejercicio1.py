#Ejercicio escribir un programa que pida la temperatura y dé una recomendación
#Luis Roberto Ardón - 20250081

temperatura = float(input("Porfa ingresa la Temperatura en °C: ")) #Asignamos la variable temperatura

if temperatura > 30 and temperatura <= 60:
    print("Hace mucho calor, fijo sos petenero men")
elif temperatura >= 15 and temperatura <=30: 
    print("El clima es agradable")
elif temperatura > 10 and temperatura < 15:
    print("Hace demasiado frio, fijo estás en Xela bro.")
else: 
    print("Fijo no vivis en Guate bro")

print("Temperatura registrada: ", temperatura, "°C") 