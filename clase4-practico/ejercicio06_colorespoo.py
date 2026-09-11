class Color:
    """Un color con nombre y componentes RGB."""

    def __init__(self, nombre, r, g, b):
        self.nombre = nombre
        self.r = r
        self.g = g
        self.b = b

    def luminosidad(self):
        """Fórmula de luminosidad percibida."""
        return 0.299 * self.r + 0.587 * self.g + 0.114 * self.b

    def es_claro(self):
        """True si la luminosidad supera 128 (usa el método anterior)."""
        return self.luminosidad() > 128

    def hex(self):
        """Devuelve el color en formato #RRGGBB."""
        return f"#{self.r:02X}{self.g:02X}{self.b:02X}"


colores = [
    Color("blanco", 255, 255, 255),
    Color("negro", 0, 0, 0),
    Color("rojo", 220, 20, 60),
    Color("celeste", 135, 206, 235),
]

# Muestro nombre, hexadecimal y si es claro u oscuro de cada color
for color in colores:
    if color.es_claro():
        tipo = "claro"
    else:
        tipo = "oscuro"
    print(f"{color.nombre}: {color.hex()} - {tipo}")