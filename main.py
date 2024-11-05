import pygame
import sys
from startup import bg_sprite


# Initialised the pygame library
pygame.init()

# Defining the screen width and height
screen_width, screen_height = 240, 160

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    screen.blit(bg_sprite)

    pygame.display.flip()
    



pygame.quit()
sys.exit()
