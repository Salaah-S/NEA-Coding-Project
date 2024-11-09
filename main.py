import pygame
import sys
import player


# Initialised the pygame library
pygame.init()

# Defining the screen width and height
screen_width, screen_height = 537, 358

screen = pygame.display.set_mode((screen_width, screen_height))


user = player.Character('red', 'boy',"assests/red_walking.png" )
user_frame = user.idle()

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

    if keys[pygame.K_DOWN]:
        user_frame, x, y = user.walking('down', x, y, speed)
    elif keys[pygame.K_UP]:
        user_frame, x, y = user.walking('up', x, y, speed)
    elif keys[pygame.K_LEFT]:
        user_frame, x, y = user.walking('left', x, y, speed)
    elif keys[pygame.K_RIGHT]:
        user_frame, x, y = user.walking('right', x, y, speed)

    screen.blit(user_frame, (x,y))
  
    pygame.display.flip()
    
    clock.tick(30)


pygame.quit()
sys.exit()
