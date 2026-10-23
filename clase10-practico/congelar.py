import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No pude abrir la camara")
    raise SystemExit

congelado = False
ultimo = None          # el último cuadro que llegó de la cámara

while True:
    # Si está congelado, no se le pide nada a la cámara
    if not congelado:
        ok, frame = cap.read()
        if not ok:
            break
        ultimo = cv2.flip(frame, 1)

    # Se escribe sobre una COPIA: así "ultimo" queda limpio
    # y al descongelar no queda el cartel pegado.
    salida = ultimo.copy()
    if congelado:
        cv2.putText(salida, "CONGELADO", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (63, 255, 182), 2)
    cv2.imshow("camara", salida)

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == ord("q"):
        break
    elif tecla == ord(" "):
        congelado = not congelado

cap.release()
cv2.destroyAllWindows()