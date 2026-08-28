"""
Presupuesto de impresión
Una imprenta cobra $450 el metro cuadrado.
"""

PRECIO_M2 = 450

# 1. Pedir ancho y alto en centímetros
ancho = float(input("Ancho de la pieza (cm): "))
alto = float(input("Alto de la pieza (cm): "))

# 2. Calcular la superficie en metros cuadrados (1 m2 = 10.000 cm2)
superficie_cm2 = ancho * alto
superficie_m2 = superficie_cm2 / 10000

# 3. Calcular el precio
precio = superficie_m2 * PRECIO_M2

# 4. Si mide más de 2 m2, recargo del 15% por manipulación
# 5. Si mide menos de 0.5 m2, cobrar un mínimo de $300
aclaracion = "Precio normal"

if superficie_m2 > 2:
    precio = precio * 1.15
    aclaracion = "Se aplicó recargo del 15% por manipulación"
elif superficie_m2 < 0.5:
    if precio < 300:
        precio = 300
        aclaracion = "Se aplicó el mínimo de $300"

# 6. Mostrar el precio final y aclarar si se aplicó recargo o mínimo
print(f"\nSuperficie: {superficie_m2:.2f} m²")
print(f"Precio final: ${precio:.2f}")
print(f"Aclaración: {aclaracion}")