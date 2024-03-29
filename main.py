import pygame
import random
import Explosion
import samuraiMain

def main():
    # Inicializar Pygame
    pygame.init()

    # Definir las dimensiones de la pantalla
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Juego de plataformas")

    # Creacion del obstaculo
    obstacle_width = 50
    obstacle_height = 50
    obstacle_x = SCREEN_WIDTH - obstacle_width
    obstacle_y = SCREEN_HEIGHT - obstacle_height
    obstacle_speed = 3
    obstacle_counter = 0
    obstacle_color = (255, 255, 255)

    # Cargar el fondo de imagen JPEG
    background_image = pygame.image.load('Background/samurai.gif').convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # Definir los colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # importar el sprite del samurai principal
    show_image = True
    walking = False
    walking_inversed = False
    jumping = False
    attack = False
    obs_destroyed = False
    pos_x = 0
    pos_y = 340

    sprite_sheet_walk = pygame.image.load('Samurai/Walk.png').convert_alpha()
    main_samurai = samuraiMain.SamuraiSprite(sprite_sheet_walk)
    sprite_sheet_walk_inverted = pygame.image.load('Samurai/Walk_inverted.png').convert_alpha()
    main_samurai_inverted = samuraiMain.SamuraiSprite(sprite_sheet_walk_inverted)
    sprite_sheet_jump = pygame.image.load('Samurai/Jump.png').convert_alpha()
    jump_samurai = samuraiMain.SamuraiSprite(sprite_sheet_jump)
    sprite_sheet_attack = pygame.image.load('Samurai/Attack_1.png').convert_alpha()
    attack_samurai = samuraiMain.SamuraiSprite(sprite_sheet_attack)
    explosions = 10
    explosion_list = []
    for i in range(explosions):
        explosion_list.append(pygame.image.load(f'Circle_explosion/Circle_explosion{i+1}.png').convert_alpha())
    main_explosion = Explosion.ExplosionSprite()
    main_explosion.animation_list(explosion_list)

    #creando los loops de la animación de caminado
    animation_list = []
    animation_list_inverted = []
    jump_list = []
    attack_list = []
    animation_steps = 9
    attack_steps = 4
    last_update = pygame.time.get_ticks()
    animation_cooldown = 75
    explosion_cooldown = 100
    frame = 0

    main_samurai.animation_list(animation_steps, animation_list)
    main_samurai_inverted.animation_list(animation_steps, animation_list_inverted)
    jump_samurai.animation_list(animation_steps, jump_list)
    attack_samurai.animation_list(attack_steps, attack_list)
    # Definir el estado del juego
    game_over = False
    background_x=0
    puntaje=0
    game_over_screen = True


    # Loop principal del juego
    while not game_over:
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
            walking_inversed = False
            jumping = False
            attack = False
            walking = True
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame = (frame +1) % animation_steps
                last_update = current_time
                if frame >= len(animation_list):
                    frame = 0
            # muestra la animación del samurai caminando en la posicion 0 0 de la pantalla
            background_x-=0.5
            bg_width = background_image.get_width()
            if background_x <= -bg_width:
                background_x = 0

        if keys[pygame.K_LEFT]:
            show_image = False
            walking = False
            jumping = False
            attack = False
            walking_inversed = True
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame = (frame + 1) % animation_steps
                last_update = current_time
                if frame >= len(animation_list):
                    frame = 0
            # muestra la animación del samurai caminando hacia la izquierda en la posicion 0, 340 de la pantalla
            background_x += 0.5
            bg_width = background_image.get_width()
            if background_x > 0:
                background_x = -bg_width
            obstacle_speed *= 0.995

        if keys[pygame.K_UP]:
            show_image = False
            walking = False
            attack = False
            jumping = True
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame = (frame + 1) % animation_steps
                last_update = current_time
                if frame >= len(jump_list):
                    frame = 0

        if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
            show_image = False
            walking = False
            walking_inversed = False
            jumping = False
            attack = True
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame = (frame + 1) % attack_steps
                last_update = current_time
                if frame >= len(attack_list):
                    frame = 0

        if keys[pygame.K_SPACE]:
            show_image = False
            walking = False
            walking_inversed = False
            jumping = False
            attack = True
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame = (frame + 1) % attack_steps
                last_update = current_time
                if frame >= len(attack_list):
                    frame = 0

        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP]and not keys[pygame.K_SPACE]:
            show_image = True
        # Crear una superficie de texto
        font = pygame.font.SysFont("IMPACT", 36)
        text_surface = font.render('Puntaje:' + str(puntaje), True, WHITE)

        # Obtener las dimensiones de la superficie de texto
        text_rect = text_surface.get_rect()

        # Definir la posición del texto
        text_x = SCREEN_WIDTH - text_rect.width - 10  # 10 es la separación desde el borde derecho de la pantalla
        text_y = 10  # 10 es la separación desde el borde superior de la pantalla
        # Pintar el fondo
        for i in range(-1, SCREEN_WIDTH // background_image.get_width() + 1):
            screen.blit(background_image, (background_x + i * background_image.get_width(), 0))
            screen.blit(text_surface, (text_x, text_y))

        # Pintar el samurai
        if show_image:
            pos_y = 340
            screen.blit(animation_list[0], (0, 340))
        elif walking and not show_image and not walking_inversed and not jumping and not attack:
            if frame < len(animation_list):
                screen.blit(animation_list[frame], (0, 340))
                pos_y = 340
            else:
                screen.blit(animation_list[frame], (0, 340))
                pos_y = 340
                walking = False
        elif walking_inversed and not show_image and not walking and not jumping and not attack:
            if frame < len(animation_list):
                screen.blit(animation_list_inverted[frame], (0, 340))
                pos_y = 340
            else:
                screen.blit(animation_list_inverted[frame], (0, 340))
                pos_y = 340
                walking_inversed = False

        elif attack and not show_image and not walking and not jumping and not walking_inversed:
            if frame < len(attack_list):
                screen.blit(attack_list[frame], (0, 340))
                pos_y = 340
            else:
                screen.blit(animation_list[frame], (0, 340))
                pos_y = 340
                attack = False
        elif jumping:
            pos_y = 100
            if frame < len(jump_list):
                if frame == (explosions-1) or frame == 0 or frame == 1:
                    screen.blit(jump_list[frame], (0, 340))
                    pos_y = 340
                else:
                    screen.blit(jump_list[frame], (0, 285))

        else:
            pass

        # Dibujar el obstáculo
        pygame.draw.rect(screen, obstacle_color, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        # Mover el obstáculo hacia la izquierda
        obstacle_x -= obstacle_speed

        # Verificar si el obstáculo se choca con el samurai
        if (obstacle_x < 100 and obstacle_y > 340) and (pos_x == 0 and pos_y == 340):
            game_over = True

        if (obstacle_x < 100 and obstacle_y > 340) and (pos_x == 0 and pos_y == 340) and attack:
            game_over = False
            puntaje = puntaje + 1
            obstacle_x = SCREEN_WIDTH
            obstacle_y = SCREEN_HEIGHT - obstacle_height
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= explosion_cooldown:
                frame = (frame + 1) % explosions
                last_update = current_time
                if frame >= explosions:
                    frame = 0
            screen.blit(explosion_list[frame], (100, 300))
            if obstacle_counter <= 10:
                obstacle_speed = random.randint(3, 8)
            elif obstacle_counter > 10:
                obstacle_speed = random.randint(3, 15)
            attack = False





        # Verificar si el obstáculo ha salido de la pantalla y reposicionarlo si es necesario
        if obstacle_x < -obstacle_width:
            obstacle_x = SCREEN_WIDTH
            obstacle_y = SCREEN_HEIGHT - obstacle_height
            if obstacle_counter != 0 and obstacle_counter <= 10:
                obstacle_speed = random.randint(3, 8)
            elif obstacle_counter != 0 and obstacle_counter > 10:
                obstacle_speed = random.randint(3, 15)
            obstacle_counter += 1

        # Actualizar la pantalla
        pygame.display.update()

    while game_over_screen:
        screen.fill(BLACK)
        font = pygame.font.SysFont("IMPACT", 48)
        screen.blit(background_image, (0, 0))
        text_surface = font.render('Puntaje final: ' + str(puntaje), True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)
        fin = font.render('GAME OVER', True, WHITE)
        text_rect2 = fin.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5))
        screen.blit(fin, text_rect2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_screen = False

    # Salir del juego
    pygame.quit()


if __name__ == '__main__':
      main()