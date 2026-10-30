import cv2, pygame, vision

# Una tecla -> (nombre, función). Mismo molde que el diccionario de filtros.
DETECTORES = {
    pygame.K_1: ("Color", vision.detectar_color),
    pygame.K_2: ("Cara", vision.detectar_cara),
    pygame.K_3: ("Mano", vision.detectar_mano),
}
nombre, detectar = DETECTORES[pygame.K_1]

# La cámara y su tamaño
cap = cv2.VideoCapture(0)
ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# La ventana, del mismo tamaño que el cuadro
pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("El espejo que reacciona")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("arial", 28)

andando = True
while andando:
    # --- eventos ---
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            andando = False
        elif e.type == pygame.KEYDOWN and e.key in DETECTORES:
            nombre, detectar = DETECTORES[e.key]

    # --- leer, espejar, detectar (después del flip) ---
    ok, frame = cap.read()
    if not ok:
        break
    frame = cv2.flip(frame, 1)
    pos = detectar(frame)          # llama a la función guardada

    # --- dibujar ---
    sup = pygame.image.frombuffer(frame.tobytes(), (ancho, alto), "BGR")
    pantalla.blit(sup, (0, 0))

    # El círculo va después del blit, si no el cuadro lo tapa
    if pos is not None:
        pygame.draw.circle(pantalla, (182, 255, 63), pos, 40, 6)
    else:
        aviso = fuente.render(f"{nombre}: no veo nada", True, (255, 80, 80))
        pantalla.blit(aviso, (10, 40))

    # Nombre del detector activo, arriba a la izquierda
    titulo = fuente.render(nombre, True, (255, 255, 255))
    pantalla.blit(titulo, (10, 8))

    pygame.display.flip()
    reloj.tick(30)

cap.release()
pygame.quit()