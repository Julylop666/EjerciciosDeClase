import cv2, pygame
from datetime import datetime
import filtros

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No pude abrir la camara")
    raise SystemExit

ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Espejo con filtros")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 48)

# Las claves son los códigos de pygame; pygame.K_1 vale 49, igual que ord("1").
# Con pygame sí se pueden usar tildes.
FILTROS = {
    pygame.K_1: ("Normal", filtros.sin_filtro),
    pygame.K_2: ("Gris", filtros.a_gris),
    pygame.K_3: ("Desenfoque", filtros.desenfocar),
    pygame.K_4: ("Bordes", filtros.bordes),
    pygame.K_5: ("Umbral", filtros.umbral),
    pygame.K_6: ("Lápiz", filtros.lapiz),
}
nombre, filtro = FILTROS[pygame.K_1]
salida = None

andando = True
while andando:
    # 1. eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            andando = False
        elif e.type == pygame.KEYDOWN:
            if e.key in FILTROS:
                nombre, filtro = FILTROS[e.key]
            elif e.key == pygame.K_s and salida is not None:
                archivo = datetime.now().strftime("captura_%Y%m%d_%H%M%S.png")
                cv2.imwrite(archivo, salida)
                print("Guardada", archivo)

    # 2. leer, espejar, filtrar
    ok, frame = cap.read()
    if not ok:
        break
    frame = cv2.flip(frame, 1)
    salida = filtro(frame)
    salida = filtros.a_color(salida)      # siempre 3 canales antes de frombuffer

    # 3. del cuadro a una superficie de pygame
    sup = pygame.image.frombuffer(
        salida.tobytes(), (ancho, alto), "BGR")
    pantalla.blit(sup, (0, 0))

    # 4. el nombre del filtro, con pygame (color en RGB)
    texto = fuente.render(nombre, True, (182, 255, 63))
    pantalla.blit(texto, (20, 20))

    pygame.display.flip()
    reloj.tick(30)

cap.release()
pygame.quit()