import pygame
import sys
import player


# Initialised the pygame library
pygame.init()

# Defining the screen width and height
screen_width, screen_height = 720, 480

screen = pygame.display.set_mode((screen_width, screen_height))


# The user controlled character
user = player.Character('red', 'boy',"assests/red_walking.png", screen_width, screen_height)
previous = 0
user_frame = user.idle(previous)

object = player.Character('green', 'girl', 'assests/green_walking.png', screen_width, screen_height)
object.frame = object.idle(previous)

x, y = 100,100


# To control the frame rate
clock = pygame.time.Clock()


running = True
while running:
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    user_frame, x, y, previous = user.walking(keys, x, y, previous)


    screen.blit(user_frame, (x,y))
    screen.blit(object.frame, (200, 200))


    pygame.display.flip()

    clock.tick(20)


pygame.quit()
sys.exit()
