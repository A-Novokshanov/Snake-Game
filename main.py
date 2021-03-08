##
##
## The goal of this project is develop an initial and fundamental understanding of machine learning
## ....with no machine learning background
## Idea taken from:
## https://www.edureka.co/blog/snake-game-with-pygame/#install
## https://towardsdatascience.com/today-im-going-to-talk-about-a-small-practical-example-of-using-neural-networks-training-one-to-6b2cbd6efdb3
## https://betterprogramming.pub/10-great-programming-projects-to-improve-your-resume-and-learn-to-program-74b14d3e9e16
##
##


#setup the game
import pygame
import random
import time

pygame.init()

maxX = 400
maxY = 300

screen = pygame.display.set_mode((maxX, maxY))
pygame.display.update()
pygame.display.set_caption('Snake Game ML')
game_over = False

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

x = maxX / 2
y = maxY / 2

initPos = [x, y, 10, 10]

foodLocation = [0,0,10,10]

x1_change = 0
y1_change = 0

score = 0

pos = initPos

clock = pygame.time.Clock()

foodPresent = False

invalidDirection = None

snake = [initPos]

while not game_over:

    ## Snake head is currently on food, increasing score and "eating" food
    if (foodPresent and (pos == foodLocation)):
        score += 1
        foodPresent = False

    ## No food is present on the board, so new food is made
    elif (not foodPresent):

        foodX = 10 * random.randint(0, (maxX / 10))
        foodY = 10 * random.randint(0, (maxY / 10))
        while (foodLocation[0] == pos[0] and foodLocation[1] == pos[1]):
            foodX = 10 * random.randint(0, (maxX / 10))
            foodY = 10 * random.randint(0, (maxY / 10))

        foodLocation = [foodX,foodY,10,10]
        foodPresent = True


    ## Takes in action interrupt
    for event in pygame.event.get():
        #print(event)  # prints out all the actions that take place on the screen


        if (event.type == pygame.QUIT):
            game_over = True

        if (event.type == pygame.KEYDOWN):
            if ((score == 0) or (event.key != invalidDirection)):
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                    invalidDirection = pygame.K_RIGHT
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                    invalidDirection = pygame.K_LEFT
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                    invalidDirection = pygame.K_DOWN
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
                    invalidDirection = pygame.K_UP

    #print(pos)

    x += x1_change
    y += y1_change

    ## Checks if snake is out of bounds
    if ((x < -10) or (y < -10) or (x > (maxX + 5)) or (y > maxY)):
        break

    snake.append(pos)

    ## Checks size of snake before adjusting parts of body
    if (len(snake) > (score + 1)):
        snake.pop(0)

    ## Snake head hits part of body causing game over
    for part in snake[: -1]:
        if part == snake[-1]:
            print(score)
            time.sleep(1)
            pygame.quit()


    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, foodLocation)
    for partPos in snake:
        pygame.draw.rect(screen, WHITE, partPos)
    pygame.display.update()


    pos = [x, y, pos[2], pos[3]]

    clock.tick(10)


print(score)

time.sleep(1)

pygame.quit()
quit()