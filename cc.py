import pygame
from pygame.locals import *
from time import *

pygame.init() 
screen = pygame.display.set_mode((600,600))
player_x = 200
player_y = 200

keys = [False,False,False,False]
player = pygame.image.load("rocket.png")
background = pygame.image.load("background.png")

while player_y < 600:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #iIF IT IS TO QUIT THE GAME
            pygame.quit()
            exit(0)
        #Check if any keyboard button is pressed
        if event.type == pygame.KEYDOWN:
            #check withch button is pressed
            if event.key == pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_LEFT:
                keys[1] = True
            elif event.key == pygame.K_DOWN:
                keys[2] = True
            elif event.key == pygame.K_RIGHT:
                keys[3] = True
            
        #check if any keyboard button is released
        if event.type == pygame.KEYUP:
            #check which button is released
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_DOWN:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False

    #if the up button is pressed
    if keys[0]:
        if player_y > 0:  #if the coordinates is greater than 0
            player_y -=7 #Change the y position by 7 pixels, The player moves upside
    elif keys[2]:
        if player_y < 536:  #if the coordinate is less than the height of the playing field
            player_y += 7   
    
    #update the x position
    #of the left key is pressed
    if keys[1]:
        if player_x > 0:
            player_x -= 2
    elif keys[3]:
        if player_x < 536:
            player_x += 2

    player_y +=5 
    sleep(0.05)

print("Game Over!")       



    
