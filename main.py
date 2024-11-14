import pygame
import sys
import player


# Initialised the pygame library
pygame.init()

# Defining the screen width and height
screen_width, screen_height = 759, 506

screen = pygame.display.set_mode((screen_width, screen_height))


user = player.Character('red', 'boy',"assests/gary.png", screen_width, screen_height)
previous = 0
user_frame = user.idle(previous)

x, y = 100,100
speed = 8

# To control the frame rate
clock = pygame.time.Clock()


running = True
while running:
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    user_frame, x, y, previous = user.walking(keys, x, y, speed, previous)


    screen.blit(user_frame, (x,y))


    pygame.display.flip()

    clock.tick(20)


pygame.quit()
sys.exit()
