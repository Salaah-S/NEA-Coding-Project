import pygame

class Spritesheet:
    def __init__(self, image):
        self.sheet = pygame.image.load(image).convert_alpha()

    def get_sprite(self, frame, width, height, scale, colorkey):
        sprite = pygame.Surface((width, height)).convert_alpha()
        sprite.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
        sprite = pygame.transform.scale(sprite, ((width * scale), (height* scale)))
        sprite.set_colorkey(colorkey)

        return sprite
    
class Tiles(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, scale):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.image = pygame.transform.scale(self.image, ((16*scale), (16*scale)))
    