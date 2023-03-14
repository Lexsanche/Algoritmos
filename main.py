import pygame
import samuraiMain


def main():
    # Inicializar Pygame
    pygame.init()

    # Definir las dimensiones de la pantalla

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Juego de plataformas")
    # Cargar el fondo de imagen JPEG
    background_image = pygame.image.load('Background/fondo.jpg').convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # Definir los colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # importar el sprite del samurai principal
    show_image = True
    sprite_sheet_walk = pygame.image.load('Samurai/Walk.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet_walk)

    #creando los loops de la animación de caminado
    animation_list = []
    animation_steps = 9
    last_update = pygame.time.get_ticks()
    animation_cooldown = 75
    frame = 0

    main_samurai.animation_list(animation_steps, animation_list)
    # Definir el estado del juego
    game_over = False

    # Loop principal del juego
    while not game_over:
        # Pintar el fondo negro
        screen.blit(background_image, (0, 0))
        if show_image:
            screen.blit(animation_list[0], (0, 340))

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            show_image = False
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame = (frame + 1) % animation_steps
                last_update = current_time
                if frame >= len(animation_list):
                    frame = 0
            # muestra la animación del samurai caminando en la posicion 0 0 de la pantalla
            screen.blit(animation_list[frame], (0, 340))
        if not keys[pygame.K_RIGHT]:
            show_image = True

        # Actualizar la pantalla
        pygame.display.update()

    # Salir del juego
    pygame.quit()


if __name__ == '__main__':
    main()
