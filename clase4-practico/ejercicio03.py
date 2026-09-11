def anio_valido(anio):
    """True si el año está entre 1800 y 2026."""
    return anio >= 1800 and anio <= 2026


def pedir_anio():
    """Pide un año y sigue pidiendo hasta que sea válido. Retorna el año, no lo imprime."""
    while True:
        anio = int(input("Año: "))
        # Un return adentro de un while corta el bucle y termina la función al mismo tiempo
        if anio_valido(anio):
            return anio
        print("Año inválido, tiene que estar entre 1800 y 2026.")


anio_ingresado = pedir_anio()
print(f"Año válido: {anio_ingresado}")