import pygame

# Definir los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class SamuraiSprite:

    def __init__(self, img):
        self.sheet = img

    def get_image(self, frame, width, height, scale, color):
        img = pygame.Surface((width, height)).convert_alpha()
        img.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        img = pygame.transform.scale(img, (width * scale, height * scale))
        img.set_colorkey(color)

        return img

    def animation_list(self, animation_steps, animation_list):
        for i in range(animation_steps):
            animation_list.append(self.get_image(i, 128, 171, 2, BLACK))
