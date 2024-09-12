edad = int(input("Introduce tu edad: "))
if edad < 4:
    precio = 0  # Entrada gratis
elif 4 <= edad <= 18:
    precio = 5  # Precio para clientes entre 4 y 18 años
else:
    precio = 10  # Precio para clientes mayores de 18 años
if precio == 0:
    print("La entrada es gratis.")
else:
    print(f"El precio de la entrada es ${precio}.")
