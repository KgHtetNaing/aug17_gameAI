#lab1
 # Example file showing a basic pygame "game loop"
import pygame
from pygame.draw import circle, line , rect , polygon
from pygame.math import Vector2
width = 1920        
height = 1080


# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

radius = 100
color_red= (255,50,50)
color_cyan = (0,255,255)
color_purple = (128, 0, 128)
color_green  = (0, 255, 0)

six_six = Vector2 (600,600)
sevenfive_six = Vector2 (750,600)
sixfive_seven = Vector2 (650,700)
nine_six = Vector2 (900,600)
nine_nine = Vector2 (900,900)
six_nine = Vector2 (600,900)
cyan_vel = Vector2(0,0)
purple_vel = Vector2(0,0)
green_vel = Vector2(0,0)
acc = Vector2(1,1)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # RENDER YOUR GAME HERE

    #transform
    #cyan Poly movement
    cyan_vel = cyan_vel + (acc[0], acc[1]-2)
    cyan_pos = cyan_vel

    #purple poly movement
    purple_vel = purple_vel + (acc[0]-2,acc[1]-2)
    purple_pos = purple_vel

    #green poly movement
    green_vel = green_vel +(acc[0]+2,acc[1]-1)
    green_pos = green_vel


    
    polygon(screen, color_cyan, [(six_six + cyan_pos),(sevenfive_six+ cyan_pos),(sixfive_seven+cyan_pos)],0)    
    polygon(screen, color_purple, [(sixfive_seven + purple_pos), (nine_six + purple_pos), (nine_nine + purple_pos), (sixfive_seven + purple_pos)],0)
    polygon(screen, color_green, [(six_six + green_pos), (nine_nine + green_pos), (six_nine+green_pos)],0)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    

pygame.quit()

