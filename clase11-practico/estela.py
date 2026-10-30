import cv2, pygame, vision

# Con la mano se dibuja con la punta del índice.
# Sin una mano a mano, cambiá por vision.detectar_color.
detectar = vision.detectar_mano

cap = cv2.VideoCapture(0)
ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Dibujar en el aire (b = borrar)")
reloj = pygame.time.Clock()

puntos = []          # la estela: arranca vacía

andando = True
while andando:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            andando = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_b:
            puntos = []                      # borrar todo

    ok, frame = cap.read()
    if not ok:
        break
    frame = cv2.flip(frame, 1)
    pos = detectar(frame)

    if pos is not None:
        puntos.append(pos)                   # al final de la lista
    puntos = puntos[-40:]                    # solo los últimos 40

    sup = pygame.image.frombuffer(frame.tobytes(), (ancho, alto), "BGR")
    pantalla.blit(sup, (0, 0))

    if len(puntos) >= 2:                     # lines pide al menos dos
        pygame.draw.lines(pantalla, (182, 255, 63), False, puntos, 6)

    pygame.display.flip()
    reloj.tick(30)

cap.release()
pygame.quit()