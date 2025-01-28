import pygame
import sys
import player
import spritesheet
from pytmx.util_pygame import load_pygame


# Initialised the pygame library
pygame.init()



class Main_Game():
    def __init__(self, screen_width, screen_height, tile_size):
        # Here, declaring the screen 
        self.screen = pygame.display.set_mode((screen_width, screen_height))

        self.tile_size = tile_size
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Adding the states
        self.game_speed = 20

        self.game_loop_state = False
        self.start_menu_state = True
        self.title_screen_state = True
        self.settings_state = False

        
        
        self.all_sprites = spritesheet.Camera(self.screen)
        self.import_maps()
        self.setup(self.tmx_maps['world'], 'house')


    def start_menu(self,key_press):
        self.screen.fill('black')

        logo = spritesheet.Spritesheet('assets/logo.png').get_sprite(0,172, 104,3, (255,255,255))
        logo_rect = logo.get_rect(center=(720, 200))

    
        play_text = self.font_writing('Press Shift', "assets/dark_font.png")
        count = 0
        for text in play_text:
            self.screen.blit(text,((count+640),400) )
            count+=(6*4)
        
        self.screen.blit(logo, logo_rect)

        if key_press[pygame.K_LSHIFT] or key_press[pygame.K_RSHIFT]:
            self.start_menu_state = False
    
    def title_screen(self, key_press):
        
        self.screen.fill('black')
        save_text = self.font_writing('New Game    Press A', 'assets/dark_font.png')
        settings_text = self.font_writing('Settings    Press B', 'assets/dark_font.png')

        count = 0
        for text in save_text:
            self.screen.blit(text,((count+150),150) )
            count+=(6*4)
        count = 0
        for text in settings_text:
            self.screen.blit(text,((count+150),300) )
            count+=(6*4)

        if key_press[pygame.K_a]:
            self.game_loop_state = True
            self.title_screen_state = False
        elif key_press[pygame.K_b]:
            self.settings_state = True
            self.title_screen_state = False
   
    def settings(self, key_press):
        self.screen.fill('black')

    
        text_speed_text = self.font_writing('Select Text Speed','assets/dark_font.png' )
        count = 0
        for text in text_speed_text:
            self.screen.blit(text,((count+150),150) )
            count+=(6*4)

        speed = {
            28: 'Slow',
            20: 'Fast'
        }
        current_speed = speed[self.game_speed]
        speed_options = self.font_writing(f"{current_speed}    Press A to change", 'assets/dark_font.png')
        count = 0
        for text in speed_options:
            self.screen.blit(text,((count+100),300) )
            count+=(6*4)

        exit_text = self.font_writing("Press Return to save", "assets/dark_font.png")
        count = 0
        for text in exit_text:
            self.screen.blit(text,((count+90),400) )
            count+=(6*4)


        if key_press[pygame.K_a]:
            if self.game_speed == 20:
                self.game_speed = 28
            else:
                self.game_speed = 20
        elif key_press[pygame.K_RETURN]:
            self.title_screen_state = True
            self.settings_state = False

    def font_writing(self, text, font):
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
        text_loc = spritesheet.Spritesheet(font)
        i = 0
        for letter in text.upper():
            num = letter_dict[letter]
            text_img.append(text_loc.get_sprite(num,6,9,4,(0,0,0)))
            i+=1
        return text_img

    def import_maps(self):
        self.tmx_maps = {'world': load_pygame('assets/map/world.tmx')}
    
    def setup(self, tmx_map, player_start_pos):
        # for ground level
        for x,y, surf in tmx_map.get_layer_by_name('Ground').tiles():
            spritesheet.Tiles((x*self.tile_size,y*self.tile_size), surf, self.all_sprites, 2)
        
        # for the upper ground level
        for x,y,surf in tmx_map.get_layer_by_name('Upper Ground').tiles():
            spritesheet.Tiles((x*self.tile_size, y*self.tile_size), surf, self.all_sprites,2)
        
        # for the grass tiles
        for obj in tmx_map.get_layer_by_name('Grass'):
            spritesheet.Tiles((obj.x, obj.y), obj.image, self.all_sprites, 2)

        # for the entities
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                if obj.properties['Position'] == player_start_pos:
                    self.x, self.y = obj.x, obj.y
                    self.user = player.Character(self.x, self.y,'assets/character/red_walking.png', self.screen_width, self.screen_height, self.tile_size)
            else:
                self.all_sprites.add(player.NPC(obj.x*2, obj.y*2, f'assets/character/{obj.name}.png', self.screen_width, self.screen_height, self.tile_size))

    def game_loop(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            if self.start_menu_state:
                self.start_menu(keys)
            elif self.title_screen_state:
                self.title_screen(keys)
            elif self.settings_state:
                self.settings(keys)

            elif self.game_loop_state:

                self.user.update(keys)
                
                self.all_sprites.draw(self.x, self.y)
                # self.obstacles.draw(self.screen)

                self.screen.blit(self.user.image, self.user.rect)
                self.x, self.y = self.user.rect.x, self.user.rect.y
                


            pygame.display.flip()

            clock.tick(self.game_speed)


        pygame.quit()
        sys.exit()



game = Main_Game(spritesheet.screen_width, spritesheet.screen_height, spritesheet.tile_size)
game.game_loop()
