# Pido al usuario la medida base en centímetros
medida = float(input("Ingrese la medida base en cm: "))

# Recorro los multiplicadores del 1 al 10 con for + range
# range(1, 11) porque el segundo número de range() nunca se incluye
for i in range(1, 11):
    resultado = medida * i
    # En cada línea aviso si el resultado supera los 100 cm
    if resultado > 100:
        print(f"{i} x {medida} = {resultado} cm (supera los 100 cm)")
    else:
        print(f"{i} x {medida} = {resultado} cm")