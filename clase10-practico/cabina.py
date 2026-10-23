import time
import cv2
import numpy as np

SEGUNDOS = 3        # duración de cada cuenta regresiva
CANTIDAD = 4        # fotos por tira
ANCHO_F, ALTO_F = 320, 240

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No pude abrir la camara")
    raise SystemExit

fotos = []
contando = False
inicio = 0.0


def armar_tira(fotos):
    """Las fotos, una abajo de la otra, de 320 x 240 cada una."""
    tira = np.full((ALTO_F * len(fotos), ANCHO_F, 3), 255, dtype=np.uint8)
    for i, foto in enumerate(fotos):
        chica = cv2.resize(foto, (ANCHO_F, ALTO_F))
        tira[i * ALTO_F:(i + 1) * ALTO_F, 0:ANCHO_F] = chica
    return tira


def texto_centrado(img, texto, escala, grosor, color):
    fuente = cv2.FONT_HERSHEY_SIMPLEX
    (w, h), _ = cv2.getTextSize(texto, fuente, escala, grosor)
    x = (img.shape[1] - w) // 2
    y = (img.shape[0] + h) // 2
    cv2.putText(img, texto, (x, y), fuente, escala, color, grosor)


while True:
    ok, frame = cap.read()
    if not ok:
        break
    frame = cv2.flip(frame, 1)
    limpio = frame.copy()          # la foto se guarda sin el número encima

    if contando:
        pasado = time.time() - inicio
        if pasado >= SEGUNDOS:
            # llegó a cero: se guarda la foto
            fotos.append(limpio)
            print("Foto", len(fotos), "de", CANTIDAD)
            if len(fotos) == CANTIDAD:
                tira = armar_tira(fotos)
                cv2.imwrite("tira.png", tira)
                cv2.imshow("tira", tira)
                print("Guardada tira.png")
                fotos = []
                contando = False
            else:
                inicio = time.time()       # arranca la cuenta siguiente
        else:
            numero = SEGUNDOS - int(pasado)    # 3, 2, 1
            texto_centrado(frame, str(numero), 8, 15, (63, 255, 182))
            cv2.putText(frame, f"Foto {len(fotos) + 1} de {CANTIDAD}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    else:
        cv2.putText(frame, "Espacio para empezar", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("cabina", frame)

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == ord("q"):
        break
    elif tecla == ord(" ") and not contando:
        fotos = []
        contando = True
        inicio = time.time()

cap.release()
cv2.destroyAllWindows()