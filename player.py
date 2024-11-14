import spritesheet
import pygame

class Character():
    def __init__(self, name, gender, sprite_loc, screen_width, screen_height):
        self.name = name
        self.gender = gender
        self.sprite_loc = sprite_loc
        self.current_frame = 1
        self.screen_width = screen_width
        self.screen_height = screen_height

    def idle(self, key):
        sprite = spritesheet.Spritesheet(self.sprite_loc)
        keys = {
            pygame.K_DOWN : 1,
            pygame.K_UP : 4,
            pygame.K_LEFT : 7,
            pygame.K_RIGHT: 10,
            0:1
        }

        return sprite.get_sprite(keys.get(key), 16,22,3)


    def walking(self, direction, x, y, speed, previous):
        sprite = spritesheet.Spritesheet(self.sprite_loc)
        
        if direction[pygame.K_DOWN]:
            
            animation_list = []
            for i in range(3):
                animation_list.append(sprite.get_sprite(i, 16,22,3))
            idle_frame = sprite.get_sprite(1, 16,22,3)
            animation_list.append(idle_frame)

            now = animation_list[self.current_frame]
            y += speed
            if y > self.screen_height - 22:
                y = self.screen_height - 22
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0

            previous = pygame.K_DOWN

        elif direction[pygame.K_UP]:
        
            animation_list = []
            for i in range(3):
                animation_list.append(sprite.get_sprite((i+3), 16,22,3))
            idle_frame = sprite.get_sprite(4, 16,22,3)
            animation_list.append(idle_frame)

            now = animation_list[self.current_frame]
            y -= speed
            if y < 0:
                y = 0
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0

            previous = pygame.K_UP

        elif direction[pygame.K_LEFT]:
        
            animation_list = []
            for i in range(3):
                animation_list.append(sprite.get_sprite((i+6), 16,22,3))
            idle_frame = sprite.get_sprite(7, 16,22,3)
            animation_list.append(idle_frame)

            now = animation_list[self.current_frame]
            x -= speed
            if x < 0:
                x = 0
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0

            previous = pygame.K_LEFT

        elif direction[pygame.K_RIGHT]:
        
            animation_list = []
            for i in range(3):
                animation_list.append(sprite.get_sprite((i+9), 16,22,3))
            idle_frame = sprite.get_sprite(10, 16,22,3)
            animation_list.append(idle_frame)            

            now = animation_list[self.current_frame]
            x += speed
            if x > self.screen_width - 16:
                x = self.screen_width - 16
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0

            previous = pygame.K_RIGHT

        else:
            now = self.idle(previous)

        return now, x, y, previous