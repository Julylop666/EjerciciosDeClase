paleta = []

while True:
    print("1. Agregar 2. Ver")
    print("3. Borrar 4. Stats")
    print("5. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        # Agrego un color nuevo al final de la lista
        color = input("Color: ")
        paleta.append(color)

    elif opcion == "2":
        # Muestro la paleta numerada desde 1, aunque Python la guarda desde 0
        if len(paleta) == 0:
            print("La paleta está vacía.")
        else:
            numero = 1
            for color in paleta:
                print(f"{numero}. {color}")
                numero = numero + 1

    elif opcion == "3":
        # Borro un color por el número que ve el usuario (desde 1)
        # Python cuenta desde 0, así que hay que restar 1 para el índice real
        if len(paleta) == 0:
            print("La paleta está vacía.")
        else:
            numero = int(input("Número a borrar: "))
            indice = numero - 1
            if indice >= 0 and indice < len(paleta):
                paleta.pop(indice)
                print("Color borrado.")
            else:
                print("Ese número no existe.")

    elif opcion == "4":
        # Estadísticas: cantidad de colores y cuál tiene el nombre más largo
        # (mismo patrón "buscar el más largo" que se vio en la teoría)
        if len(paleta) == 0:
            print("La paleta está vacía.")
        else:
            print(f"Cantidad de colores: {len(paleta)}")
            mas_largo = paleta[0]
            for color in paleta:
                if len(color) > len(mas_largo):
                    mas_largo = color
            print(f"El nombre más largo es: {mas_largo}")

    elif opcion == "5":
        break

    else:
        print("Opción inválida")