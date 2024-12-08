import pygame
import sys
import player


# Initialised the pygame library
pygame.init()

# Defining the screen width, height and setting the display screen
screen_width, screen_height= 720, 480
tile_size = 32

x, y = 240,160


class Main_Game():
    def __init__(self, screen_width, screen_height, tile_size):
        # Here, declaring the screen 
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.start_menu_state = True
        self.user = player.Character(x,y,'assests/red_walking.png', screen_width, screen_height, tile_size)
        oak = player.Character(120,160, 'assests/oak.png', screen_width, screen_height, tile_size)
        self.obstacle = pygame.sprite.Group()
        self.obstacle.add(oak)

    def start_menu(self,key_press):
        font = pygame.font.Font(None, 60)
        
        play_text = font.render('PRESS SHIFT', True, 'white')
        play_rect = play_text.get_rect(center=(360,240))

        self.screen.fill('black')
        self.screen.blit(play_text, play_rect)
        if key_press[pygame.K_LSHIFT] or key_press[pygame.K_RSHIFT]:
            self.start_menu_state = False
        else:
            self.start_menu_state == True
    
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
