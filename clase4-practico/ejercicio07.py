class Material:
    """Un material del inventario, con nombre, precio unitario y stock."""

    def __init__(self, nombre, precio_unitario, stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock

    def valor_total(self):
        """Precio unitario por stock."""
        return self.precio_unitario * self.stock

    def hay_stock(self):
        """True si queda al menos una unidad."""
        return self.stock >= 1

    def consumir(self, cantidad):
        """Si alcanza, descuenta del stock y devuelve True. Si no, no hace nada y devuelve False."""
        if cantidad <= self.stock:
            self.stock = self.stock - cantidad
            return True
        return False


papel = Material("papel A3", 15, 100)
tinta = Material("tinta negra", 800, 5)

# Pruebo los tres métodos con dos materiales distintos
print(f"Valor total del papel: {papel.valor_total()}")
print(f"¿Hay stock de tinta?: {tinta.hay_stock()}")

# Pruebas del método consumir con mensajes claros
exito_papel = papel.consumir(30)
print(f"Consumo de 30 unidades de papel exitoso: {exito_papel} (Stock restante: {papel.stock})")

exito_tinta = tinta.consumir(10)
print(f"Consumo de 10 unidades de tinta exitoso: {exito_tinta} (Stock restante: {tinta.stock})")