import pygame

# Definir los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class ExplosionSprite:
    def __init__(self):
        self.img = []

    def get_image(self, frame, width, height, scale, color):
        img = pygame.Surface((width, height)).convert_alpha()
        img.blit(self.img[frame], (0, 0))
        img = pygame.transform.scale(img, (width * scale, height * scale))
        img.set_colorkey(color)
        return img

    def animation_list(self, imgn):
        for i in imgn:
            self.img.append(i)
