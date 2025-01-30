import spritesheet
import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self, x, y, loc, screen_width, screen_height, walking_speed, collision):
        super().__init__()
        self.walking_speed = walking_speed*2
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.previous = 0 
        self.loc = spritesheet.Spritesheet(loc)
        self.sprites = []
        for i in range(12):
            self.sprites.append(self.loc.get_sprite((i), 16,32,2, (34,177,76)))
            if i == 2 or i == 5 or i == 8 or i == 11:
                self.sprites.append(self.loc.get_sprite(i-1, 16,32,2, (34,177,76)))


        self.current_frame = 1

        self.image = self.sprites[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.previous_position = self.rect.center

        self.vertical = self.screen_height//(2*self.walking_speed)
        self.horizontal = self.screen_width//(2.5*self.walking_speed)
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y + self.rect.height // 2, self.rect.width, self.rect.height // 2)
        self.collision = collision

    def update(self, direction):
        self.previous_position = self.hitbox.topleft  # Save previous position

        # Get initial frame for animation
        self.current_frame = (self.current_frame + 1) % 4

        # Vertical movement
        if direction[pygame.K_UP]:
            self.previous = pygame.K_UP
            self.hitbox.y -= self.vertical  # Move first

            # Check for collisions
            for sprite in self.collision:
                if sprite.hitbox.colliderect(self.hitbox):
                    self.hitbox.top = sprite.hitbox.bottom  # Prevent movement

            self.rect.topleft = self.hitbox.topleft  # Sync rect with hitbox
            self.image = self.sprites[self.current_frame + 4]

        elif direction[pygame.K_DOWN]:
            self.previous = pygame.K_DOWN
            self.hitbox.y += self.vertical  # Move first

            for sprite in self.collision:
                if sprite.hitbox.colliderect(self.hitbox):
                    self.hitbox.bottom = sprite.hitbox.top

            self.rect.topleft = self.hitbox.topleft
            self.image = self.sprites[self.current_frame]

        # Horizontal movement
        elif direction[pygame.K_LEFT]:
            self.previous = pygame.K_LEFT
            self.hitbox.x -= self.horizontal  # Move first

            for sprite in self.collision:
                if sprite.hitbox.colliderect(self.hitbox):
                    self.hitbox.left = sprite.hitbox.right

            self.rect.topleft = self.hitbox.topleft
            self.image = self.sprites[self.current_frame + 8]

        elif direction[pygame.K_RIGHT]:
            self.previous = pygame.K_RIGHT
            self.hitbox.x += self.horizontal  # Move first

            for sprite in self.collision:
                if sprite.hitbox.colliderect(self.hitbox):
                    self.hitbox.right = sprite.hitbox.left

            self.rect.topleft = self.hitbox.topleft
            self.image = self.sprites[self.current_frame + 12]

        # If no movement, idle animation
        else:
            self.image = self.sprites[self.idle(self.previous)]
    
    def idle(self, key):

        keys = {
            pygame.K_DOWN : 1,
            pygame.K_UP : 5,
            pygame.K_LEFT : 9,
            pygame.K_RIGHT: 13,
            0:1
        }
        return keys[key]
    
    def encounter_check(self, grp):
        for grass in grp:
            if grass.hitbox.colliderect(self.hitbox):
                return True









class NPC(Character):
    def __init__(self, x, y, loc, screen_width, screen_height, walking_speed, collision):
        super().__init__(x, y, loc, screen_width, screen_height, walking_speed, collision=None)
