import pygame
import sys
import player


# Initialised the pygame library
pygame.init()

# Defining the screen width and height
screen_width, screen_height = 720, 480

screen = pygame.display.set_mode((screen_width, screen_height))

x, y = 240,160

# The user controlled character
user = player.Character(x,y,'assests/red_walking.png', screen_width, screen_height)

oak = player.Character(120,160, 'assests/oak.png', screen_width, screen_height)
obstacle = pygame.sprite.Group()
obstacle.add(oak)

# To control the frame rate
clock = pygame.time.Clock()


running = True
while running:
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    user.update(keys, obstacle)
    screen.blit(user.image, user.rect)
    obstacle.draw(screen)


    pygame.display.flip()

    clock.tick(20)


pygame.quit()
sys.exit()
