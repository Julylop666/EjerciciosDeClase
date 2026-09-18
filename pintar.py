"""Ejercicio 5.3: clic para pintar.

Cada clic agrega un círculo de color al azar en esa posición.
La barra espaciadora vacía la lista. La X cierra la ventana.
"""
import pygame
import random

pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Ejercicio 5.3 - Pintar")
reloj = pygame.time.Clock()

NAVY = (20, 22, 43)
PALETA = [
    (230, 60, 60),   # rojo
    (60, 200, 90),   # verde
    (250, 210, 40),  # amarillo
    (60, 130, 230),  # azul
]

RADIO = 15
circulos = []  # cada elemento: (x, y, color)

andando = True
while andando:
    # 1. Escuchar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            andando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            color = random.choice(PALETA)
            circulos.append((evento.pos[0], evento.pos[1], color))
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                circulos = []

    # 2. Actualizar: no hay lógica extra en este ejercicio

    # 3. Dibujar (la lista se redibuja entera cada vuelta)
    pantalla.fill(NAVY)
    for cx, cy, color in circulos:
        pygame.draw.circle(pantalla, color, (cx, cy), RADIO)
    pygame.display.flip()

    # 4. Esperar
    reloj.tick(60)

pygame.quit()