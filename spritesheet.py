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
    
    def pkmn_sprite(self, column, row):
        sprite = pygame.Surface((64,64)).convert_alpha()
        start_loc = ((130*column),34+(165*row))
        colorkey = self.sheet.get_at(start_loc)
        sprite.blit(self.sheet, (0,0), (start_loc[0], start_loc[1], 64, 64))
        sprite = pygame.transform.scale(sprite, ((64*3), (64*3)))
        sprite.set_colorkey(colorkey)
        return sprite
    
    def name_box(self):
        sprite = pygame.Surface((104,34)).convert_alpha()
        colorkey = self.sheet.get_at((0,0))
        sprite.blit(self.sheet, (0,0))
        sprite = pygame.transform.scale(sprite, ((104*5), (34*5)))
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
        self.x_offset = -(player_pos[0]+16-screen_width//(2))
        self.y_offset = -(player_pos[1]+32-screen_height//(2))

        for sprite in self:
            self.display_surface.blit(sprite.image, (sprite.rect.x + self.x_offset, sprite.rect.y + self.y_offset))
       
class BorderSprite(Tiles):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy()

def font_writing(text, font):
        
        letter_dict = {
            'A':0,
            'B':1,
            'C':2,
            'D':3,
            'E':4,
            'F':5,
            'G':6,
            'H':7,
            'I':8,
            'J':9,
            'K':10,
            'L':11,
            'M':12,
            'N':13,
            'O':14,
            'P':15,
            'Q':16,
            'R':17,
            'S':18,
            'T':19,
            'U':20,
            'V':21,
            'W':22,
            'X':23,
            'Y':24,
            'Z':25, 
            ' ':26
        }

        text_img = []
        text_loc = Spritesheet(font)
        i = 0
        colorkey = (0,0,0) if font == 'assets/dark_font.png' else (255,255,255)
        
        for letter in text.upper():
            num = letter_dict[letter]
            text_img.append(text_loc.get_sprite(num,6,9,4,colorkey))
            i+=1
        return text_img


def draw_bar(surface, rect, value, max_value, color, bg_color, radius = 1):
	ratio = rect.width / max_value
	bg_rect = rect.copy()
	progress = max(0, min(rect.width,value * ratio))
	progress_rect = pygame.FRect(rect.topleft, (progress,rect.height))
	pygame.draw.rect(surface, bg_color, bg_rect, 0, radius)
	pygame.draw.rect(surface, color, progress_rect, 0, radius)