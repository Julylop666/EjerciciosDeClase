# Ejercicio 9.1 - Reporte de la carpeta fotos/
import cv2, os

# Trabajar siempre desde la carpeta de este archivo, esté donde esté la terminal
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def orientacion(ancho, alto):
    """Devuelve 'horizontal', 'vertical' o 'cuadrada'."""
    if ancho > alto:
        return "horizontal"
    if ancho < alto:
        return "vertical"
    return "cuadrada"


for nombre in sorted(os.listdir("fotos")):
    # Quedarse solo con las imágenes
    if not nombre.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img = cv2.imread(os.path.join("fotos", nombre))

    # imread no da error si falla: devuelve None. Lo salteamos.
    if img is None:
        print(f"{nombre}: no se pudo abrir, la salteo")
        continue

    # shape es (alto, ancho, canales): el alto va primero
    alto, ancho = img.shape[:2]
    proporcion = ancho / alto

    print(f"{nombre}: {ancho} x {alto} | proporcion {proporcion:.2f} | "
          f"{orientacion(ancho, alto)}")