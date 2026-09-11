stock = {"papel": 120, "tinta negra": 8,
         "tinta color": 3, "cartón": 45,
         "cinta": 0}


def hay_stock(stock, material):
    """True si el material existe en el stock y tiene más de 0 unidades."""
    # .get() con default 0 evita el KeyError si el material no está en el diccionario
    return stock.get(material, 0) > 0


def faltantes(stock, minimo):
    """Lista de materiales con menos de 'minimo' unidades."""
    resultado = []
    for material, cantidad in stock.items():
        if cantidad < minimo:
            resultado.append(material)
    return resultado


def total_unidades(stock):
    """Suma de todas las unidades del stock."""
    total = 0
    for cantidad in stock.values():
        total = total + cantidad
    return total


# Pruebo hay_stock con un material que NO está en el diccionario
print(f"¿Hay stock de goma? (no existe): {hay_stock(stock, 'goma')}")
print(f"¿Hay stock de papel?: {hay_stock(stock, 'papel')}")
print(f"¿Hay stock de cinta?: {hay_stock(stock, 'cinta')}")
print(f"Faltantes (menos de 10): {faltantes(stock, 10)}")
print(f"Total de unidades: {total_unidades(stock)}")