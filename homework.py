#lab1
 # Example file showing a basic pygame "game loop"
import pygame
from pygame.draw import circle, line , rect , polygon
from pygame.math import Vector2
import random
width = 1280        
height = 720


# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True


color_cyan = (0,255,255)
color_purple = (128, 0, 128)
color_green  = (0, 255, 0)

six_six = Vector2 (600,600)
sevenfive_six = Vector2 (750,600)
sixfive_seven = Vector2 (650,700)
nine_six = Vector2 (900,600)
nine_nine = Vector2 (900,900)
six_nine = Vector2 (600,900)
cyan_vel = Vector2(1,-2)
cyan_pos = Vector2(0,0)
purple_vel = Vector2(-2,-2)
purple_pos = Vector2(0,0)
green_vel = Vector2(3,5)
green_pos = Vector2(0,0)
c_fill = g_fill = p_fill = 0





while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # RENDER YOUR GAME HERE
    #random function
    def random_state():
      color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
      fill = random.randint(0, 1)
      return color,fill
    
    #transform
    #cyan Poly movement
   
    cyan_pos = cyan_pos + cyan_vel
    cyan_movement = [(six_six + cyan_pos),(sevenfive_six+ cyan_pos),(sixfive_seven+cyan_pos)]
    
    cyan_xs = [c.x for c in cyan_movement]
    cyan_ys = [c.y for c in cyan_movement]

    min_cx,max_cx = min(cyan_xs), max(cyan_xs)
    min_cy,max_cy = min(cyan_ys), max(cyan_ys)
    print (min_cx)

    if min_cx <= 0:
        cyan_vel.x=cyan_vel.x*-1
        cyan_pos = cyan_pos+(-min_cx,0)
        color_cyan,c_fill = random_state()
    elif max_cx>= width:
        cyan_vel.x=cyan_vel.x*-1
        cyan_pos = cyan_pos+(width-max_cx,0)     
        color_cyan,c_fill = random_state()
    
    if min_cy <= 0:
        cyan_vel.y=cyan_vel.y*-1
        cyan_pos = cyan_pos+(0,-min_cy)
        color_cyan,c_fill = random_state()
    elif max_cy >= height:
          cyan_vel.y=cyan_vel.y*-1
          cyan_pos=cyan_pos+(0,height-max_cy)
          color_cyan,c_fill = random_state()

    #purple poly movement
    
    purple_pos = purple_pos+purple_vel
    purple_movement = [(sixfive_seven + purple_pos), (nine_six + purple_pos), (nine_nine + purple_pos), (sixfive_seven + purple_pos)]

    
    p_xs = [p.x for p in purple_movement]
    p_ys = [p.y for p in purple_movement]

    min_px,max_px = min(p_xs), max(p_xs)
    min_py,max_py = min(p_ys), max(p_ys)

    if min_px <= 0:
         purple_vel.x*= -1
         purple_pos.x +=-min_px
         color_purple,p_fill = random_state()

    elif max_px >= width:
         purple_vel.x*=-1
         purple_pos.x += width-max_px
         color_purple,p_fill = random_state()

    if min_py <= 0:
         purple_vel.y*=-1
         purple_pos.y += -min_py
         color_purple,p_fill = random_state()

    elif max_py >= height:
         purple_vel.y*=-1
         purple_pos.y += height-max_py
         color_purple,p_fill = random_state()
               

    #green poly movement
    
    green_pos = green_pos+green_vel
    green_movement = [(six_six + green_pos), (nine_nine + green_pos), (six_nine+green_pos)]
   
    g_xs = [g.x for g in green_movement]
    g_ys = [g.y for g in green_movement]

    min_gx,max_gx = min(g_xs), max(g_xs)
    min_gy,max_gy = min(g_ys), max(g_ys)

    if min_gx <= 0:
         green_vel.x*= -1
         green_pos.x += -min_gx
         color_green,g_fill = random_state()

    elif max_gx >= width:
         green_vel.x*=-1
         green_pos.x += width-max_gx
         color_green,g_fill = random_state()

    if min_gy <= 0:
         green_vel.y*=-1
         green_pos.y += -min_gy
         color_green,g_fill = random_state()

    elif max_gy >= height:
         green_vel.y*=-1
         green_pos.y += height-max_gy
         color_green,g_fill = random_state()

     

         


    
    polygon(screen, color_cyan, cyan_movement,c_fill)    
    polygon(screen, color_purple, purple_movement ,p_fill)
    polygon(screen, color_green, green_movement ,g_fill)

   
    
    
   
    

    


   

# flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    

pygame.quit()

