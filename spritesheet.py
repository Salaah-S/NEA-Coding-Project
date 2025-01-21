import pygame

# Defining the screen width, height and setting the display screen
tile_size = 16
screen_width, screen_height= 1440, 480


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
        self.x = pos[0]*scale
        self.y = pos[1]*scale
        self.image = surf
        self.rect = self.image.get_frect(topleft = (self.x, self.y))
        self.image = pygame.transform.scale(self.image, ((tile_size*scale), (tile_size*scale)))
    
class Camera(pygame.sprite.Group):
    def __init__(self, surf):
        super().__init__()
        self.display_surface = surf
        

    def draw(self, player_x, player_y):
        self.x_offset = -(player_x-screen_width//(3*tile_size))
        self.y_offset = -(player_y-screen_height//(3*tile_size))

        for sprite in self:
            self.display_surface.blit(sprite.image, (sprite.rect.x + self.x_offset, sprite.rect.y + self.y_offset))