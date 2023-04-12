import pygame

# Definir los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class ExplosionSprite:

    def __init__(self, imgn):
        self.img = []
        self.img = imgn

    def get_image(self, frame, width, height, scale, color):
        img = pygame.Surface((width, height)).convert_alpha()
        img.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        img = pygame.transform.scale(img, (width * scale, height * scale))
        img.set_colorkey(color)
        return img

    def animation_list(self, animation_steps, imgn):
        for i in range(animation_steps):
            self.img.append(imgn[i])
