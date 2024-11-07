import pygame
import sys


# Initialised the pygame library
pygame.init()

# Defining the screen width and height
screen_width, screen_height = 537, 358

screen = pygame.display.set_mode((screen_width, screen_height))


class Spritesheet:
    def __init__(self, filename):
        
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((255,255,255))
        sprite.blit(self.sprite_sheet, (0,0), (x,y,w,h))
        return sprite

my_spritesheet = Spritesheet('assests/red_walking.png')
trainer_1 = pygame.transform.scale(my_spritesheet.get_sprite(16,0,16,32), (48,96))
# The transform.scale is used to make the character bigger, so that it is visible

player_x, player_y = 240,160
speed = 250  # Pixels per second

# Create a clock object to control the frame rate
clock = pygame.time.Clock()


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    # Calculate time passed since last frame
    delta_time = clock.tick(60) / 1000.0 

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # delta_time for consistent speed
    if keys[pygame.K_LEFT]:
        player_x -= speed * delta_time
    if keys[pygame.K_RIGHT]:
        player_x += speed * delta_time
    if keys[pygame.K_UP]:
        player_y -= speed * delta_time
    if keys[pygame.K_DOWN]:
        player_y += speed * delta_time


    screen.fill("grey")
    screen.blit(trainer_1, (player_x,player_y))

    pygame.display.flip()
    



pygame.quit()
sys.exit()
