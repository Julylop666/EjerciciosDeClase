# ETAPA A: catálogo de obras usando diccionarios

def agregar_obra(catalogo):
    """Pide los datos y agrega la obra."""
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = int(input("Año: "))
    precio = float(input("Precio: "))
    obra = {"titulo": titulo, "autor": autor, "anio": anio, "precio": precio}
    catalogo.append(obra)


def listar_obras(catalogo):
    """Muestra las obras numeradas."""
    if len(catalogo) == 0:
        print("El catálogo está vacío.")
        return
    numero = 1
    for obra in catalogo:
        print(f"{numero}. {obra['titulo']} - {obra['autor']} ({obra['anio']}) - ${obra['precio']}")
        numero = numero + 1


def buscar_por_autor(catalogo, autor):
    """Devuelve las obras de ese autor."""
    encontradas = []
    for obra in catalogo:
        if obra["autor"] == autor:
            encontradas.append(obra)
    return encontradas


def estadisticas(catalogo):
    """Devuelve cantidad, total y promedio (no imprime nada)."""
    cantidad = len(catalogo)
    total = 0
    for obra in catalogo:
        total = total + obra["precio"]
    if cantidad == 0:
        promedio = 0
    else:
        promedio = total / cantidad
    return {"cantidad": cantidad, "total": total, "promedio": promedio}


catalogo = []

while True:
    print("1. Agregar   2. Listar")
    print("3. Buscar    4. Stats")
    print("5. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        agregar_obra(catalogo)
    elif opcion == "2":
        listar_obras(catalogo)
    elif opcion == "3":
        # La opción 3 pide el autor antes de llamar a la función
        autor = input("Autor a buscar: ")
        resultado = buscar_por_autor(catalogo, autor)
        if len(resultado) == 0:
            print("No se encontraron obras de ese autor.")
        else:
            for obra in resultado:
                print(f"- {obra['titulo']} ({obra['anio']})")
    elif opcion == "4":
        # La opción 4 recibe el diccionario que retorna estadisticas() y lo muestra
        stats = estadisticas(catalogo)
        print(f"Cantidad: {stats['cantidad']}")
        print(f"Total: ${stats['total']}")
        print(f"Promedio: ${stats['promedio']}")
    elif opcion == "5":
        break
    else:
        print("Opción inválida")