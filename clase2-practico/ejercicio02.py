"""
Conversor de medidas
Pide una medida en centímetros y la convierte a pulgadas y milímetros.
"""

# 1. Pedir una medida en centímetros
cm = float(input("Ingresá una medida en centímetros: "))

# 2. Convertir a pulgadas y a milímetros
pulgadas = cm / 2.54
milimetros = cm * 10

# 3. Redondear las dos a dos decimales
pulgadas = round(pulgadas, 2)
milimetros = round(milimetros, 2)

# 4. Ver si entra en un marco estándar de 30 cm
if cm <= 30:
    resultado_marco = "entra"
else:
    resultado_marco = "no entra"

# Mostrar resultado
print(f"\n{cm} cm equivalen a {pulgadas} pulgadas y {milimetros} mm")
print(f"¿Entra en un marco de 30 cm? {resultado_marco}")