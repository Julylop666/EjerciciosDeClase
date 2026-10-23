import cv2
import numpy as np


# ---------------------------------------------------------------
# De la clase 9
# ---------------------------------------------------------------
def cargar(ruta):
    img = cv2.imread(ruta)
    if img is None:
        print("No pude cargar", ruta)
    return img


def miniatura(img, ancho=200):
    alto = int(img.shape[0] * ancho / img.shape[1])
    return cv2.resize(img, (ancho, alto))


def a_gris(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# ---------------------------------------------------------------
# Clase 10
# ---------------------------------------------------------------
def sin_filtro(img):
    return img


def desenfocar(img):
    return cv2.GaussianBlur(img, (21, 21), 0)


def bordes(img):
    gris = a_gris(img)
    return cv2.Canny(gris, 100, 200)


def umbral(img):
    gris = a_gris(img)
    _, bn = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)
    return bn


def invertir(img):
    return 255 - img


def lapiz(img):
    """Dibujo a lápiz, en cuatro pasos."""
    gris = a_gris(img)                                # 1. gris
    negativo = 255 - gris                             # 2. invertir
    borroso = cv2.GaussianBlur(negativo, (21, 21), 0) # 3. desenfocar
    return cv2.divide(gris, 255 - borroso, scale=256) # 4. mezclar


def a_color(img):
    """Si la imagen tiene 1 canal, la pasa a 3. Si no, la devuelve igual."""
    if len(img.shape) == 2:
        return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img