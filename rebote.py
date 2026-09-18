"""Ejercicio 5.2: el círculo que rebota.

El círculo arranca en el centro y se mueve solo, en diagonal,
rebotando en los cuatro bordes de la ventana.
"""
import pygame

pygame.init()

ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 5.2 - Rebote")
reloj = pygame.time.Clock()

NAVY = (20, 22, 43)
LIMA = (182, 255, 63)

RADIO = 25
x, y = ANCHO // 2, ALTO // 2
vel_x, vel_y = 4, 3

andando = True
while andando:
    # 1. Escuchar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            andando = False

    # 2. Actualizar
    x += vel_x
    y += vel_y

    # el borde lo toca el borde del círculo, no el centro:
    # por eso se compara contra x +- RADIO, no contra x solo
    if x - RADIO < 0 or x + RADIO > ANCHO:
        vel_x = -vel_x
    if y - RADIO < 0 or y + RADIO > ALTO:
        vel_y = -vel_y

    # 3. Dibujar
    pantalla.fill(NAVY)
    pygame.draw.circle(pantalla, LIMA, (x, y), RADIO)
    pygame.display.flip()

    # 4. Esperar
    reloj.tick(60)

pygame.quit()