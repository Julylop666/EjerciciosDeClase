# Ejercicio 9.3 - Hoja de contactos
import cv2, os
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

COLUMNAS = 3
LADO = 200   # cada foto queda de 200 x 200


def recorte_cuadrado(img):
    """Recorta el cuadrado del centro de la imagen."""
    alto, ancho = img.shape[:2]
    lado = min(alto, ancho)      # el cuadrado más grande que entra
    y0 = (alto - lado) // 2      # lo que sobra se reparte a ambos lados
    x0 = (ancho - lado) // 2
    return img[y0:y0 + lado, x0:x0 + lado]


# 1. Cargar todas las imágenes que se puedan abrir
fotos = []
for nombre in sorted(os.listdir("fotos")):
    if not nombre.lower().endswith((".jpg", ".jpeg", ".png")):
        continue
    img = cv2.imread(os.path.join("fotos", nombre))
    if img is None:
        print(f"{nombre}: no se pudo abrir, la salteo")
        continue
    # 2. Primero se recorta al cuadrado y DESPUÉS se achica: así no se deforma
    cuadrada = recorte_cuadrado(img)
    fotos.append(cv2.resize(cuadrada, (LADO, LADO), interpolation=cv2.INTER_AREA))

# 3. Filas necesarias, redondeando para arriba: 4 fotos -> 2 filas
filas = (len(fotos) + COLUMNAS - 1) // COLUMNAS

# 4. Hoja blanca: donde sobra lugar queda blanco (255 = todo de todo)
hoja = np.full((filas * LADO, COLUMNAS * LADO, 3), 255, dtype=np.uint8)

for i, foto in enumerate(fotos):
    fila = i // COLUMNAS    # división entera: cada 3 fotos, baja una fila
    col = i % COLUMNAS      # resto: 0, 1, 2, 0, 1, 2...
    y = fila * LADO
    x = col * LADO
    hoja[y:y + LADO, x:x + LADO] = foto

# 5. Guardar
cv2.imwrite("contacto.png", hoja)
print(f"Hoja de contactos: {len(fotos)} fotos en {filas} filas")