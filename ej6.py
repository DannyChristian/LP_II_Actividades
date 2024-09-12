altura = int(input("Introduce un número entero para la altura del triángulo: "))
for i in range(1, altura + 1):
    fila = [str(j) for j in range(2 * i - 1, 0, -2)]
    print(" ".join(fila))
