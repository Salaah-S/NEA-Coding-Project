import pygame
import sys


# Initialised the pygame library
pygame.init()

# Defining the screen width and height
screen_width, screen_height = 240, 160

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player_sprite = 



running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    

    pygame.display.flip()
    



pygame.quit()
sys.exit()
