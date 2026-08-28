"""
¿Color claro u oscuro?
luz = 0.299*R + 0.587*G + 0.114*B
"""

# 1. Pedir R y validar antes de seguir
r = int(input("Valor R (0-255): "))

if r < 0 or r > 255:
    print("\nEl valor de R está fuera de rango. No se puede calcular.")
else:
    # Pedir G y validar antes de seguir
    g = int(input("Valor G (0-255): "))

    if g < 0 or g > 255:
        print("\nEl valor de G está fuera de rango. No se puede calcular.")
    else:
        # Pedir B y validar
        b = int(input("Valor B (0-255): "))

        # 2. Validar que B esté en el rango, con and, sin funciones
        if b >= 0 and b <= 255:
            # 3. Calcular la luminosidad
            luz = 0.299 * r + 0.587 * g + 0.114 * b

            # 4 y 5. Definir si es claro u oscuro
            if luz > 128:
                print(f"\nLuminosidad: {luz:.2f}")
                print("El color es claro: se recomienda tipografía negra")
            else:
                print(f"\nLuminosidad: {luz:.2f}")
                print("El color es oscuro: se recomienda tipografía blanca")
        else:
            print("\nEl valor de B está fuera de rango. No se puede calcular.")