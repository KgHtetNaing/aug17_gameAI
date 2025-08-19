#lab1
 # Example file showing a basic pygame "game loop"
import pygame
from pygame.draw import circle, line , rect
from pygame.math import Vector2
width = 1280
height = 720


# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

radius = 100
color_red= (255,50,50)
position = Vector2(width/2,height/2)
vel = Vector2(0,0)
acc = Vector2(1,1)
acc.x =1
acc.y =1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")
    # RENDER YOUR GAME HERE

    # vel.x = vel.x + acc.x
    # vel.y = vel.y + acc.y
    vel = vel+acc
    # position.x = position.x + vel.x
    # position.y = position.y + vel.y
    position = position+vel
    circle(screen, color_red , position , radius)

    acc.x = 0 
    acc.y = 0
    # to stop acc from increasing. Learn more

    # line(screen , (50,50,0), (300,600) , (1000, 600))
    # line(screen , (50,0,0), (300,600) , (500, 300))
    # line(screen , (50,0,0), (1000,600) , (500, 300))
    # pygame.draw.rect(screen, (0,0,0), (width/2,height/2,100,60), width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    

pygame.quit()

