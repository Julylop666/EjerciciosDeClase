import cv2, pygame

cap = cv2.VideoCapture(0)
ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Calibrar color: clic en el objeto, m = máscara")
reloj = pygame.time.Clock()

rango = None        # (minimo, maximo) una vez que se hizo clic
ver_mascara = False

andando = True
while andando:
    ok, frame = cap.read()
    if not ok:
        break
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            andando = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_m:
            ver_mascara = not ver_mascara
        elif e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            h, s, v = (int(n) for n in hsv[y, x])
            # el tono va de 0 a 179: max y min para no salirse
            h_min = max(0, h - 10)
            h_max = min(179, h + 10)
            rango = ((h_min, 100, 100), (h_max, 255, 255))
            print(f"Píxel ({x}, {y}): HSV = ({h}, {s}, {v})")
            print(f"COLOR_MIN = {rango[0]}")
            print(f"COLOR_MAX = {rango[1]}")

    if ver_mascara and rango is not None:
        mascara = cv2.inRange(hsv, rango[0], rango[1])   # 1 canal
        a_mostrar = cv2.cvtColor(mascara, cv2.COLOR_GRAY2BGR)  # a 3 canales
    else:
        a_mostrar = frame

    sup = pygame.image.frombuffer(a_mostrar.tobytes(), (ancho, alto), "BGR")
    pantalla.blit(sup, (0, 0))
    pygame.display.flip()
    reloj.tick(30)

cap.release()
pygame.quit()