def area_rectangulo(ancho, alto):
    """Devuelve el área del rectángulo."""
    return ancho * alto


def perimetro_rectangulo(ancho, alto):
    """Devuelve el perímetro del rectángulo."""
    return 2 * (ancho + alto)


def describir(ancho, alto):
    """Arma y RETORNA un texto con área, perímetro y orientación (no lo imprime)."""
    # Reutilizo las dos funciones anteriores en vez de recalcular
    area = area_rectangulo(ancho, alto)
    perimetro = perimetro_rectangulo(ancho, alto)

    if ancho > alto:
        orientacion = "horizontal"
    elif alto > ancho:
        orientacion = "vertical"
    else:
        orientacion = "cuadrado"

    return f"Área: {area} - Perímetro: {perimetro} - Orientación: {orientacion}"


# Pruebo las tres funciones con al menos tres medidas distintas
print(describir(30, 20))
print(describir(10, 40))
print(describir(15, 15))