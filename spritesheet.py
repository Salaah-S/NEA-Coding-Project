import pygame

# Defining the screen width, height and setting the display screen
tile_size = 32
screen_width, screen_height= 1280, 720


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
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.copy()
    
class Camera(pygame.sprite.Group):
    def __init__(self, surf):
        super().__init__()
        self.display_surface = surf
        

    def draw(self, player_pos):
        self.x_offset = -(player_pos[0]-screen_width//(tile_size))
        self.y_offset = -(player_pos[1]-screen_height//(tile_size))

        for sprite in self:
            self.display_surface.blit(sprite.image, (sprite.rect.x + self.x_offset, sprite.rect.y + self.y_offset))
       
class BorderSprite(Tiles):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy()