##
##
## The goal of this project is develop an initial and fundamental understanding of machine learning
## ....with no machine learning background
## Idea taken from https://www.edureka.co/blog/snake-game-with-pygame/#install
##


#setup the game
import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake Game ML')
game_over = False

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

initPos = [200,150, 10, 10]

foodLocation = [0,0,10,10]

x = 200
y = 150

x1_change = 0
y1_change = 0

pos = initPos

clock = pygame.time.Clock()

foodPresent = False

score = 0


while not game_over:

    if (foodPresent and (pos == foodLocation)):
        score += 1
        #foodPresent = False

    if (not foodPresent):

        print('broke')

        foodX = 10 * random.randint(0, 39)
        foodY = 10 * random.randint(0, 29)
        while (foodLocation[0] == pos[0] and foodLocation[1] == pos[1]):
            foodX = 10 * random.randint(0, 39)
            foodY = 10 * random.randint(0, 29)

        foodLocation = [foodX,foodY,10,10]
        foodPresent = True


    for event in pygame.event.get():
        #print(event)  # prints out all the actions that take place on the screen


        if (event.type == pygame.QUIT):
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    print(pos)

    x += x1_change
    y += y1_change

    if ((x < -10) or (y < -10) or (x > 405) or (y > 305)):
        break

    screen.fill(GRAY)
    pygame.draw.rect(screen, WHITE, pos)
    pygame.draw.rect(screen, RED, foodLocation)
    pygame.display.update()


    pos = [x, y, pos[2], pos[3]]

    clock.tick(10)


print(score)

time.sleep(1)

pygame.quit()
quit()