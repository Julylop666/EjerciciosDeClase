# ETAPA B: mismo catálogo de la etapa A, ahora con la clase Obra en vez de diccionarios

class Obra:
    """Una obra del catálogo."""

    def __init__(self, titulo, autor, anio, precio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.precio = precio

    def ficha(self):
        """Devuelve el texto de presentación de la obra."""
        return f"{self.titulo} - {self.autor} ({self.anio}) - ${self.precio}"

    def antiguedad(self):
        """Cuántos años tiene la obra."""
        return 2026 - self.anio

    def es_cara(self, limite=2000):
        """True si el precio supera el límite (2000 por defecto)."""
        return self.precio > limite


def agregar_obra(catalogo):
    """Pide los datos y agrega un objeto Obra (en vez de un diccionario)."""
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = int(input("Año: "))
    precio = float(input("Precio: "))
    catalogo.append(Obra(titulo, autor, anio, precio))


def listar_obras(catalogo):
    """Muestra las obras numeradas, usando el método ficha()."""
    if len(catalogo) == 0:
        print("El catálogo está vacío.")
        return
    numero = 1
    for obra in catalogo:
        print(f"{numero}. {obra.ficha()}")
        numero = numero + 1


def buscar_por_autor(catalogo, autor):
    """Devuelve las obras de ese autor (ahora se accede con punto, no con corchetes)."""
    encontradas = []
    for obra in catalogo:
        if obra.autor == autor:
            encontradas.append(obra)
    return encontradas


def estadisticas(catalogo):
    """Devuelve cantidad, total y promedio."""
    cantidad = len(catalogo)
    total = 0
    for obra in catalogo:
        total = total + obra.precio
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
        autor = input("Autor a buscar: ")
        resultado = buscar_por_autor(catalogo, autor)
        if len(resultado) == 0:
            print("No se encontraron obras de ese autor.")
        else:
            for obra in resultado:
                print(f"- {obra.titulo} ({obra.anio})")
    elif opcion == "4":
        stats = estadisticas(catalogo)
        print(f"Cantidad: {stats['cantidad']}")
        print(f"Total: ${stats['total']}")
        print(f"Promedio: ${stats['promedio']}")
    elif opcion == "5":
        break
    else:
        print("Opción inválida")