"""
Ficha técnica de obra
Programa que pide los datos de una obra y devuelve una ficha formateada.
"""

# 1. Pedir datos: título, autor, año, ancho en cm y alto en cm
titulo = input("Título de la obra: ")
autor = input("Autor: ")
anio = input("Año: ")
ancho = float(input("Ancho (cm): "))
alto = float(input("Alto (cm): "))

# 2. Calcular el área en cm2
area = ancho * alto

# 3. Orientación
if ancho > alto:
    orientacion = "Horizontal"
elif alto > ancho:
    orientacion = "Vertical"
else:
    orientacion = "Cuadrada"

# 4. Tamaño
if area < 1000:
    tamanio = "Chica"
elif area <= 5000:
    tamanio = "Mediana"
else:
    tamanio = "Grande"

# 5. Mostrar todo junto en una ficha prolija
print("\n" + "=" * 40)
print("FICHA TÉCNICA DE OBRA".center(40))
print("=" * 40)
print(f"Título:      {titulo}")
print(f"Autor:       {autor}")
print(f"Año:         {anio}")
print(f"Dimensiones: {ancho} cm x {alto} cm")
print(f"Área:        {area:.2f} cm²")
print(f"Orientación: {orientacion}")
print(f"Tamaño:      {tamanio}")
print("=" * 40)