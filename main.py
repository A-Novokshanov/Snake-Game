##
##
## The goal of this project is develop an initial and fundamental understanding of machine learning
## ....with no machine learning background
##
##


#setup the game
import pygame
pygame.init()

screen = pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake Game ML')
game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)  # prints out all the actions that take place on the screen

        if (event.type == pygame.QUIT):
            game_over = True
            
pygame.quit()
quit()