colores = ["rojo", "azul", "verde agua",
           "negro", "amarillo pastel",
           "gris", "violeta"]

# Colores con más de una palabra: uso split() y miro cuántos elementos tiene la lista resultante
print("Colores con más de una palabra:")
for color in colores:
    if len(color.split()) > 1:
        print(f"- {color}")

# Colores que empiezan con vocal: miro el primer carácter con color[0]
print("Colores que empiezan con vocal:")
vocales = "aeiouAEIOU"
for color in colores:
    if color[0] in vocales:
        print(f"- {color}")

# sorted() devuelve una lista NUEVA ordenada, sin modificar "colores" (a diferencia de .sort())
colores_ordenados = sorted(colores)
print("Colores ordenados alfabéticamente:")
for color in colores_ordenados:
    print(f"- {color}")

# Slicing [:3] toma los tres primeros elementos de la lista ya ordenada
print("Los tres primeros de la lista ordenada:")
for color in colores_ordenados[:3]:
    print(f"- {color}")

# Confirmo que la lista original sigue intacta
print("Lista original (sin modificar):")
print(colores)