"""Ejercicio 5.1: la ventana que cambia de color.

R -> fondo rojo, V -> fondo verde, A -> fondo azul.
Cualquier otra tecla no hace nada.
"""
import pygame

pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Ejercicio 5.1 - Fondo")
reloj = pygame.time.Clock()

NEGRO = (0, 0, 0)
ROJO = (200, 30, 30)
VERDE = (30, 180, 60)
AZUL = (30, 60, 200)

# el color vive en una variable; fill() siempre usa esta variable
color_fondo = NEGRO

andando = True
while andando:
    # 1. Escuchar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            andando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                color_fondo = ROJO
            elif evento.key == pygame.K_v:
                color_fondo = VERDE
            elif evento.key == pygame.K_a:
                color_fondo = AZUL
            # cualquier otra tecla: no hace nada

    # 2. Actualizar: no hay lógica extra en este ejercicio

    # 3. Dibujar
    pantalla.fill(color_fondo)
    pygame.display.flip()

    # 4. Esperar
    reloj.tick(60)

pygame.quit()