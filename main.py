import pygame
import sys
import player
import spritesheet


# Initialised the pygame library
pygame.init()

# Defining the screen width, height and setting the display screen
screen_width, screen_height= 720, 480
tile_size = 64

x, y = 240,160


class Main_Game():
    def __init__(self, screen_width, screen_height, tile_size):
        # Here, declaring the screen 
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.start_menu_state = True
        self.user = player.Character(x,y,'assets/character/red_walking.png', screen_width, screen_height, tile_size)
        oak = player.Character(120,160, 'assets/character/oak.png', screen_width, screen_height, tile_size)
        self.obstacle = pygame.sprite.Group()
        self.obstacle.add(oak)

    def start_menu(self,key_press):
        self.screen.fill('black')
        font = pygame.font.Font(None, 60)

        logo = spritesheet.Spritesheet('assets/logo.png').get_sprite(0,172, 104,3, (255,255,255))
        logo_rect = logo.get_rect(center=(360, 200))

        play_text = self.font_writing('Press Shift', "assets/dark_font.png")
        count = 0
        for text in play_text:
            self.screen.blit(text,((count+228),400) )
            count+=(6*4)
        

        
        self.screen.blit(logo, logo_rect)
        if key_press[pygame.K_LSHIFT] or key_press[pygame.K_RSHIFT]:
            self.start_menu_state = False
        else:
            self.start_menu_state == True
    
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


    def game_loop(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.screen.fill("grey")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            if self.start_menu_state:
                self.start_menu(keys)
            else:
                self.user.update(keys, self.obstacle)
                self.screen.blit(self.user.image, self.user.rect)
                self.obstacle.draw(self.screen)


            pygame.display.flip()

            clock.tick(20)


        pygame.quit()
        sys.exit()



game = Main_Game(screen_width, screen_height, tile_size)
game.game_loop()
