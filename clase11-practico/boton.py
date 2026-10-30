import cv2, pygame, vision

detectar = vision.detectar_mano      # punta del índice

cap = cv2.VideoCapture(0)
ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("El botón sin tocar")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("arial", 28)

boton = pygame.Rect(20, 20, 220, 70)   # arriba a la izquierda
adentro = 0                            # cuadros seguidos con la mano adentro
LIMITE = 30                            # un segundo a 30 cuadros por segundo
clics = 0

andando = True
while andando:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            andando = False

    ok, frame = cap.read()
    if not ok:
        break
    frame = cv2.flip(frame, 1)
    pos = detectar(frame)

    # suma si la posición está dentro; vuelve a 0 si sale o no hay posición
    if pos is not None and boton.collidepoint(pos):
        adentro += 1
    else:
        adentro = 0

    # == (no >=): cuenta una sola vez; para repetir hay que salir y volver a entrar
    if adentro == LIMITE:
        clics += 1
        print("clic", clics)

    sup = pygame.image.frombuffer(frame.tobytes(), (ancho, alto), "BGR")
    pantalla.blit(sup, (0, 0))

    # el botón, y la barra de progreso adentro (ancho proporcional a adentro)
    pygame.draw.rect(pantalla, (40, 40, 40), boton)
    ancho_barra = min(adentro, LIMITE) * boton.width // LIMITE
    pygame.draw.rect(pantalla, (182, 255, 63),
                     (boton.x, boton.y, ancho_barra, boton.height))
    pygame.draw.rect(pantalla, (255, 255, 255), boton, 3)

    texto = fuente.render(f"Clics: {clics}", True, (255, 255, 255))
    pantalla.blit(texto, texto.get_rect(center=boton.center))

    if pos is not None:                  # un punto para ver dónde está el dedo
        pygame.draw.circle(pantalla, (255, 80, 80), pos, 8)

    pygame.display.flip()
    reloj.tick(30)

cap.release()
pygame.quit()