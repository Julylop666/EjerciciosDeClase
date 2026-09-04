titulo = input("Ingrese el título de la obra: ")

# Cantidad de caracteres, usando len() sobre el string (un string se recorre como una lista)
print(f"Cantidad de caracteres: {len(titulo)}")

# Divido el título en palabras con split() y cuento cuántas hay
palabras = titulo.split()
print(f"Cantidad de palabras: {len(palabras)}")

# Recorro el título letra por letra y cuento las vocales (incluyendo acentos)
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
cantidad_vocales = 0
for letra in titulo:
    if letra in vocales:
        cantidad_vocales = cantidad_vocales + 1
print(f"Cantidad de vocales: {cantidad_vocales}")

# .upper() devuelve un texto nuevo en mayúsculas, no modifica el original
print(f"En mayúsculas: {titulo.upper()}")

# [::-1] da vuelta la lista de palabras, y " ".join() las vuelve a unir en un texto
palabras_invertidas = palabras[::-1]
print(f"Palabras invertidas: {' '.join(palabras_invertidas)}")