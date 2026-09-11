obras = [
    {"titulo": "Sin título", "autor": "Pérez", "anio": 2020, "precio": 1500},
    {"titulo": "Serie azul", "autor": "Gómez", "anio": 2018, "precio": 3200},
    {"titulo": "Retrato", "autor": "Pérez", "anio": 2022, "precio": 900},
    {"titulo": "Paisaje", "autor": "Díaz", "anio": 2015, "precio": 4100},
    {"titulo": "Estudio", "autor": "Gómez", "anio": 2021, "precio": 2000},
]


def obra_mas_cara(obras):
    """Devuelve el diccionario de la obra más cara (patrón 'buscar el más...' de la clase 3)."""
    mas_cara = obras[0]
    for obra in obras:
        if obra["precio"] > mas_cara["precio"]:
            mas_cara = obra
    return mas_cara


def autores(obras):
    """Lista de autores, sin repetir."""
    lista = []
    for obra in obras:
        if obra["autor"] not in lista:
            lista.append(obra["autor"])
    return lista


def obras_por_autor(obras):
    """Diccionario autor -> cantidad (patrón de contar visto en la teoría)."""
    conteo = {}
    for obra in obras:
        autor = obra["autor"]
        if autor in conteo:
            conteo[autor] = conteo[autor] + 1
        else:
            conteo[autor] = 1
    return conteo


def posteriores_a(obras, anio):
    """Obras hechas después de ese año."""
    resultado = []
    for obra in obras:
        if obra["anio"] > anio:
            resultado.append(obra)
    return resultado


print(f"Obra más cara: {obra_mas_cara(obras)['titulo']}")
print(f"Autores: {autores(obras)}")
print(f"Obras por autor: {obras_por_autor(obras)}")
print("Obras posteriores a 2019:")
for obra in posteriores_a(obras, 2019):
    print(f"- {obra['titulo']} ({obra['anio']})")