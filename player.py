import spritesheet
import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self, x, y, loc, screen_width, screen_height, tile_size):
        super().__init__()
        self.tile_size = tile_size
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.previous = 0 
        self.loc = spritesheet.Spritesheet(loc)
        self.sprites = []
        for i in range(12):
            self.sprites.append(self.loc.get_sprite((i), 16,32,3, (255,255,255)))
            if i == 2 or i == 5 or i == 8 or i == 11:
                self.sprites.append(self.loc.get_sprite(i-1, 16,32,3, (255,255,255)))


        self.current_frame = 1

        self.image = self.sprites[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.previous_position = self.rect.topleft
        
    def update(self, direction, obstacles):
        self.previous_position = self.rect.topleft

        if direction[pygame.K_UP]:
            self.previous = pygame.K_UP
            animation_list = []
            for i in range(4):
                animation_list.append(self.sprites[i+4])
            now = animation_list[self.current_frame]

            self.rect.top -= self.screen_height//self.tile_size
            if self.rect.top < 0:
                self.rect.top = 0

            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0
        
        elif direction[pygame.K_DOWN]:
            self.previous = pygame.K_DOWN
            animation_list = []
            for i in range(4):
                animation_list.append(self.sprites[i])
            now = animation_list[self.current_frame]

            self.rect.bottom += self.screen_height//self.tile_size
            if self.rect.bottom > self.screen_height:
                self.rect.bottom = self.screen_height
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0

        elif direction[pygame.K_LEFT]:
            self.previous = pygame.K_LEFT
            animation_list = []
            for i in range(4):
                animation_list.append(self.sprites[i+8])
            now = animation_list[self.current_frame]

            self.rect.left -= self.screen_width//self.tile_size
            if self.rect.left <0:
                self.rect.left = 0
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0

        elif direction[pygame.K_RIGHT]:
            self.previous = pygame.K_RIGHT
            animation_list = []
            for i in range(4):
                animation_list.append(self.sprites[i+12])
            now = animation_list[self.current_frame]

            self.rect.right += self.screen_width//self.tile_size
            if self.rect.right > self.screen_width:
                self.rect.right = self.screen_width
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0
        else:
            now = self.sprites[self.idle(self.previous)]
        
        if pygame.sprite.spritecollide(self, obstacles, False):
            self.rect.topleft = self.previous_position
        
        self.image = now
        return now
    
    def idle(self, key):

        keys = {
            pygame.K_DOWN : 1,
            pygame.K_UP : 5,
            pygame.K_LEFT : 9,
            pygame.K_RIGHT: 13,
            0:1
        }
        return keys[key]
