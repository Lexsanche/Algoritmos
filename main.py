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

    # Definir los colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # importar el sprite del samurai principal
    show_image = True
    sprite_sheet_walk = pygame.image.load('Samurai/Walk.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet_walk)

    #creando los loops de la animación de caminado
    animation_list = []
    jump_animation = []
    attack_animation_1 = []
    attack_animation_2 = []
    attack_animation_3 = []
    dead_animation = []
    hurt_animation = []
    idle_animation = []
    protection_animation = []
    run_animation = []
    animation_steps = 10
    last_update = pygame.time.get_ticks()
    animation_cooldown = 75
    frame = 0

    main_samurai.animation_list(animation_steps, animation_list)
    sprite_sheet = pygame.image.load('Samurai/Jump.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet)
    main_samurai.animation_list(animation_steps, jump_animation)
    sprite_sheet = pygame.image.load('Samurai/Attack_1.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet)
    main_samurai.animation_list(animation_steps, attack_animation_1)
    sprite_sheet = pygame.image.load('Samurai/Attack_2.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet)
    main_samurai.animation_list(animation_steps, attack_animation_2)
    sprite_sheet = pygame.image.load('Samurai/Attack_3.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet)
    main_samurai.animation_list(animation_steps, attack_animation_3)
    sprite_sheet = pygame.image.load('Samurai/Dead.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet)
    main_samurai.animation_list(animation_steps, dead_animation)
    sprite_sheet = pygame.image.load('Samurai/Hurt.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet)
    main_samurai.animation_list(animation_steps, hurt_animation)
    sprite_sheet = pygame.image.load('Samurai/Idle.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet)
    main_samurai.animation_list(animation_steps, idle_animation)
    sprite_sheet = pygame.image.load('Samurai/Protection.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet)
    main_samurai.animation_list(animation_steps, protection_animation)
    sprite_sheet = pygame.image.load('Samurai/Run.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet)
    main_samurai.animation_list(animation_steps, run_animation)

    # Definir el estado del juego
    game_over = False

    # Loop principal del juego
    while not game_over:
        # Pintar el fondo negro
        screen.fill(BLACK)
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
