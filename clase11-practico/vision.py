import cv2
import mediapipe as mp

# ---- Lo que se prepara una sola vez (al hacer import vision) ----

# Rango HSV del objeto (naranja, de la tabla de la teoría).
# Lo afinás con calibrar.py (ejercicio 11.1) y pegás acá los valores nuevos.
COLOR_MIN = (5, 120, 120)
COLOR_MAX = (20, 255, 255)

# Clasificador de Haar para caras de frente (OpenCV 4.11: el .xml viene en el paquete).
XML = "haarcascade_frontalface_default.xml"
clasificador = cv2.CascadeClassifier(cv2.data.haarcascades + XML)

# Detector de manos de MediaPipe (ruta A, 0.10.x): una sola mano, es más rápido.
manos = mp.solutions.hands.Hands(max_num_hands=1)


def detectar_color(frame):
    """Recibe un cuadro BGR. Devuelve (x, y) del centro de la mancha
    más grande del color buscado, o None."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mascara = cv2.inRange(hsv, COLOR_MIN, COLOR_MAX)
    # OpenCV 4: findContours devuelve DOS cosas (contornos y jerarquía)
    contornos, _ = cv2.findContours(
        mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contornos) == 0:          # max() de una lista vacía da error
        return None
    grande = max(contornos, key=cv2.contourArea)
    if cv2.contourArea(grande) < 500:  # muy chica: es ruido, no tu objeto
        return None
    x, y, w, h = cv2.boundingRect(grande)
    return (x + w // 2, y + h // 2)


def detectar_cara(frame):
    """Recibe un cuadro BGR. Devuelve (x, y) del centro de la primera
    cara de frente, o None."""
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    caras = clasificador.detectMultiScale(
        gris, 1.1, 5, minSize=(80, 80))
    if len(caras) == 0:              # NO usar "if caras:" (falla con numpy)
        return None
    x, y, w, h = caras[0]
    return (int(x + w // 2), int(y + h // 2))


def detectar_mano(frame):
    """Recibe un cuadro BGR. Devuelve (x, y) de la punta del índice
    (punto 8 de MediaPipe), o None."""
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   # MediaPipe espera RGB
    resultado = manos.process(rgb)
    if resultado.multi_hand_landmarks is None:     # sin mano es None, no []
        return None
    mano = resultado.multi_hand_landmarks[0]       # la primera mano
    punta = mano.landmark[8]                       # punta del índice
    alto, ancho = frame.shape[:2]                  # shape da (alto, ancho)
    x = int(punta.x * ancho)                       # de 0-1 a píxeles
    y = int(punta.y * alto)
    return (x, y)