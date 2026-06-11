#Luis Roberto Ardón y José David Franco

n = int(input("Ingresa el numero de productos que compraste: "))
total = 0
mas_caro = 0

for i in range(1, n + 1):
    precio = float(input(f"precio del producto: {i}: Q "))
    total = total + precio

    if precio > mas_caro:
        mas_caro = precio
    if total >= 500:
        descuento = total * 0.1   
    else:
        descuento = 0

print("Tu total sin descuento es:", "Q", round(total, 2))
print("Tu descuento es de:","Q", round(descuento, 2))
print("Tu total ahora es de:", "Q", round(total - descuento, 2))
print("Tu artículo más caro fue:", "Q", round(mas_caro, 2))