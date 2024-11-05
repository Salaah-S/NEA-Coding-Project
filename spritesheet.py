import pygame

class Spritesheet:
    def __init__(self, filename):
        
        # This allows the class to turn the spritesheet into the dimensions that the window might be changed into
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Suface((w,h))
        sprite.set_colorkey()
