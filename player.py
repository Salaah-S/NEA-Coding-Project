import spritesheet

class Character:
    def __init__(self, name, gender, sprite_loc):
        self.name = name
        self.gender = gender
        self.sprite_loc = sprite_loc
        self.current_frame = 1

    def idle(self):
        sprite = spritesheet.Spritesheet(self.sprite_loc)
        return sprite.get_sprite(1, 16,32,3)


    def walking(self, direction, x, y, speed):
        sprite = spritesheet.Spritesheet(self.sprite_loc)
        
        if direction == 'down':
            
            animation_list = []
            for i in range(3):
                animation_list.append(sprite.get_sprite(i, 16,32,3))
            animation_list.append(sprite.get_sprite(1, 16,32,3))

            now = animation_list[self.current_frame]
            y += speed
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0


        elif direction == 'up':
        
            animation_list = []
            for i in range(3):
                animation_list.append(sprite.get_sprite((i+3), 16,32,3))
            animation_list.append(sprite.get_sprite(3, 16,32,3))

            now = animation_list[self.current_frame]
            y -= speed
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0


        elif direction == 'left':
        
            animation_list = []
            for i in range(3):
                animation_list.append(sprite.get_sprite((i+6), 16,32,3))
            animation_list.append(sprite.get_sprite(6, 16,32,3)) 

            now = animation_list[self.current_frame]
            x -= speed
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0

        elif direction == 'right':
        
            animation_list = []
            for i in range(3):
                animation_list.append(sprite.get_sprite((i+9), 16,32,3))
            animation_list.append(sprite.get_sprite(9, 16,32,3))            

            now = animation_list[self.current_frame]
            x += speed
            self.current_frame +=1
            if self.current_frame == 4:
                self.current_frame = 0

        return now, x, y
    
