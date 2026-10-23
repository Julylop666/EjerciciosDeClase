import sys
import cv2

# En Windows, DirectShow abre y cierra la cámara sin colgarse
if sys.platform == "win32":
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
else:
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
    # Si se cerró la ventana con la X, salir también
    if cv2.getWindowProperty("camara", cv2.WND_PROP_VISIBLE) < 1:
        break
    elif tecla == ord(" "):
        congelado = not congelado

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)      # en Mac, sin esto la ventana puede quedar abierta