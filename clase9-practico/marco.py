# Ejercicio 9.2 - Marco de color con título
# Uso:  python marco.py            (usa la primera foto de fotos/)
#       python marco.py dormido.jpg (usa la foto que le digas)
import cv2, os, sys
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

BORDE = 30                     # px de marco a los costados y arriba
FRANJA = 70                    # px de franja abajo, para el título
COLOR_MARCO = (120, 60, 20)    # BGR: un azul oscuro
COLOR_TEXTO = (255, 255, 255)  # blanco
FUENTE = cv2.FONT_HERSHEY_SIMPLEX

# 1. Elegir la imagen
if len(sys.argv) > 1:
    nombre = sys.argv[1]
else:
    nombre = next(n for n in sorted(os.listdir("fotos"))
                  if n.lower().endswith((".jpg", ".jpeg", ".png")))

img = cv2.imread(os.path.join("fotos", nombre))
if img is None:
    sys.exit(f"No se pudo abrir {nombre}")

alto, ancho = img.shape[:2]

# 2. La cuenta del lienzo (hacela en papel):
#    ancho total = borde + ancho + borde
#    alto total  = borde + alto + franja
alto_lienzo = BORDE + alto + FRANJA
ancho_lienzo = BORDE + ancho + BORDE

# np.full crea una tabla llena de un mismo color. Es (alto, ancho, 3).
lienzo = np.full((alto_lienzo, ancho_lienzo, 3), COLOR_MARCO, dtype=np.uint8)

# 3. Pegar la imagen: el hueco del lienzo mide justo lo mismo que img
lienzo[BORDE:BORDE + alto, BORDE:BORDE + ancho] = img

# 4. El título es el nombre del archivo sin la extensión
base, extension = nombre.rsplit(".", 1)
titulo = base.replace("_", " ")

# Si el título no entra a lo ancho, achicar la letra de a poco
escala = 1.0
while escala > 0.3:
    (ancho_texto, _), _ = cv2.getTextSize(titulo, FUENTE, escala, 2)
    if ancho_texto <= ancho:
        break
    escala -= 0.1

# putText usa la esquina de ABAJO a la izquierda del texto como punto (x, y)
y_texto = BORDE + alto + 45
cv2.putText(lienzo, titulo, (BORDE, y_texto), FUENTE, escala,
            COLOR_TEXTO, 2, cv2.LINE_AA)

# 5. Guardar con _marco en el nombre
os.makedirs("salida", exist_ok=True)
destino = os.path.join("salida", f"{base}_marco.{extension}")
cv2.imwrite(destino, lienzo)
print("Guardado:", destino)