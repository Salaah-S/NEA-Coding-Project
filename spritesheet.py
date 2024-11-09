import pygame

class Spritesheet:
    def __init__(self, image):
        self.sheet = pygame.image.load(image).convert_alpha()

    def get_sprite(self, frame, width, height, scale):
        sprite = pygame.Surface((width, height)).convert_alpha()
        sprite.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
        sprite = pygame.transform.scale(sprite, ((width * scale), (height* scale)))
        sprite.set_colorkey((255,255,255))

        return sprite
    