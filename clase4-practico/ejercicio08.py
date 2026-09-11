class Material:
    """Un material del inventario, con nombre, precio unitario y stock (misma clase del ejercicio 4.6)."""

    def __init__(self, nombre, precio_unitario, stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock

    def valor_total(self):
        return self.precio_unitario * self.stock

    def hay_stock(self):
        return self.stock >= 1

    def consumir(self, cantidad):
        if cantidad <= self.stock:
            self.stock = self.stock - cantidad
            return True
        return False


# Lista de cinco materiales, dos de ellos sin stock
materiales = [
    Material("papel A3", 15, 100),
    Material("tinta negra", 800, 0),
    Material("cartón", 40, 45),
    Material("cinta", 60, 0),
    Material("tinta color", 950, 3),
]


# Las siguientes son funciones sueltas, FUERA de la clase
def valor_inventario(materiales):
    """Suma del valor de todos los materiales."""
    total = 0
    for material in materiales:
        total = total + material.valor_total()
    return total


def sin_stock(materiales):
    """Lista de los materiales agotados."""
    agotados = []
    for material in materiales:
        if not material.hay_stock():
            agotados.append(material)
    return agotados


def mas_caro(materiales):
    """El material de mayor precio unitario."""
    caro = materiales[0]
    for material in materiales:
        if material.precio_unitario > caro.precio_unitario:
            caro = material
    return caro


print(f"Valor del inventario: ${valor_inventario(materiales)}")
print("Sin stock:")
for material in sin_stock(materiales):
    print(f"- {material.nombre}")
print(f"Más caro: {mas_caro(materiales).nombre}")