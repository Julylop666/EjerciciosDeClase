# Lista donde voy a guardar los precios cargados
precios = []

# Repito mientras el usuario no escriba 'fin' (corte por valor centinela)
while True:
    entrada = input("Precio (o 'fin' para terminar): ")
    if entrada == "fin":
        break
    precios.append(float(entrada))

# Si no se cargó ningún precio, aviso y no calculo nada
if len(precios) == 0:
    print("No se cargó ningún precio.")
else:
    # --- Versión a mano, con acumuladores ---
    # (mismo patrón contador/acumulador que se vio en la teoría)
    total = 0
    cantidad = 0
    mas_caro = precios[0]
    mas_barato = precios[0]

    for precio in precios:
        total = total + precio
        cantidad = cantidad + 1
        if precio > mas_caro:
            mas_caro = precio
        if precio < mas_barato:
            mas_barato = precio

    promedio = total / cantidad

    print("--- Versión a mano ---")
    print(f"Cantidad de precios: {cantidad}")
    print(f"Total: {total}")
    print(f"Promedio: {promedio}")
    print(f"Más caro: {mas_caro}")
    print(f"Más barato: {mas_barato}")

    # --- Versión con sum(), max() y min() ---
    # hace lo mismo que arriba, pero usando las funciones incorporadas de Python
    print("--- Versión con sum(), max(), min() ---")
    print(f"Cantidad de precios: {len(precios)}")
    print(f"Total: {sum(precios)}")
    print(f"Promedio: {sum(precios) / len(precios)}")
    print(f"Más caro: {max(precios)}")
    print(f"Más barato: {min(precios)}")