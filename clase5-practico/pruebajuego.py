import pygame

pygame.init()

ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Ventana que cambia de color")

color_fondo = (0, 0, 0)  # negro al arrancar

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                color_fondo = (255, 0, 0)
            elif evento.key == pygame.K_v:
                color_fondo = (0, 255, 0)
            elif evento.key == pygame.K_a:
                color_fondo = (0, 0, 255)

    ventana.fill(color_fondo)
    pygame.display.flip()

pygame.quit()