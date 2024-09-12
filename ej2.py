nombre = input("Introduce tu nombre: ").capitalize()
sexo = input("Introduce tu sexo (M para mujer, H para hombre): ").upper()
if (sexo == "M" and nombre < "F") or (sexo == "H" and nombre > "O"):
    grupo = "A"
else:
    grupo = "B"
print(f"Perteneces al grupo {grupo}.")
