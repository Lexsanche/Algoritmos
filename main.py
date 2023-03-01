import pygame

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la pantalla

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de plataformas")

# Definir los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir las propiedades del jugador
player_width = 40
player_height = 60
player_x = 50
player_y = SCREEN_HEIGHT - player_height
player_speed = 5

# Definir las propiedades de la plataforma
platform_width = SCREEN_WIDTH
platform_height = 20
platform_x = 0
platform_y = SCREEN_HEIGHT - platform_height

# Definir el estado del juego
game_over = False

# Loop principal del juego
while not game_over:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover al jugador
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_height:
        player_y += player_speed

    # Detectar colisiones
    if player_y + player_height > platform_y:
        player_y = platform_y - player_height

    # Dibujar objetos en la pantalla
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [player_x, player_y, player_width, player_height])
    pygame.draw.rect(screen, BLACK, [platform_x, platform_y, platform_width, platform_height])

    # Actualizar la pantalla
    pygame.display.update()

# Salir del juego
pygame.quit()
