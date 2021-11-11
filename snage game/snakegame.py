# use pygame clock
import pygame
import random
pygame.init()
#
# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
screen_width = 900
screen_height = 600
Velocity_val = 5
#
# creating window
GameWindow = pygame.display.set_mode((screen_width, screen_height))
# title
pygame.display.set_caption('snake game')
# to display
pygame.display.update()

# make clock
clock = pygame.time.Clock()
# function make score in screen
# font variable
font = pygame.font.SysFont("None", 55)
# adding high score file
with open("high_score.txt", "r") as f:
    high_score = f.read()   # read file high score


def score_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    GameWindow.blit(screen_text, (x, y))       # screen update
#

def plot_snake(GameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(GameWindow, color, [x, y, snake_size, snake_size])

# game loop
def game_loop():
    # game element
    exit_game = False
    game_over = False
    #
    # define value of rectangle
    snake_x = 45
    snake_y = 55
    snake_size = 15
    # frame par second to use clock
    fps = 50
    # velocity
    velocity_x = 0
    velocity_y = 0
    # to improve snake length
    snake_length = 1
    snake_list = []  # to store length
    # food
    # given random value
    food_x = random.randint(20, int(screen_width / 1.5))  # 1.5 because red box not corner in corner
    food_y = random.randint(20, int(screen_height / 1.5))
    # score
    score = 0

    # adding high score file
    with open("high_score.txt", "r") as f:
        high_score = f.read()  # read file high score
    while not exit_game:
        # game over
        if game_over:
            # store high score file
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))  # read file high score
            GameWindow.fill(white)
            score_screen("Game Over ! press enter to continue :)", red, screen_width/7, screen_height/2.5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    game_loop()
        else:
            for event in pygame.event.get():
                # print(event)    # to print event arrow will move and print
                if event.type == pygame.QUIT:
                    exit_game = True
                # key performance
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # snake_x = snake_x + 10
                        velocity_x = Velocity_val
                        velocity_y = 0
                        # to move snake in X 10 is a value what problem snake move only press key so fix that problem
                        # fix that problem fir velocity
                        # remove diagonal if velocity_x = 10 so same given velocity_y=0 in same loop
                    if event.key == pygame.K_LEFT:
                        velocity_x = - Velocity_val
                        velocity_y = 0   # diagonal fix

                    if event.key == pygame.K_UP:
                        velocity_y = - Velocity_val
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = Velocity_val
                        velocity_x = 0

# because same value snake_x and velocity_x so this is not work they work as a diagonal so solve that problem use this
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

        # use to eat apple and score
            # abs absolute vale

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 1
                # print("score: ", score)  #bacause we done score in screen

                # food value change
                food_x = random.randint(20, int(screen_width / 1.5))  # 1.5 because red box not corner in corner
                food_y = random.randint(20, int(screen_height / 1.5))
                snake_length += 3            # 5 in a coordinate

                # condition for high score
                if score > int(high_score):
                    high_score = score
            GameWindow.fill(white)             # change color
            # food loop
            pygame.draw.rect(GameWindow, red, [food_x, food_y, snake_size, snake_size])
            score_screen("score : " + str(score) + '  High score : ' + str(high_score), red, 5, 5)  # add score function
        # snake_list is empty so
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            # game over in snake head
            if head in snake_list[:-1]:
                game_over = True
            # game over condition in wall
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
               # print("game_over")
            # to create rectangle
            pygame.draw.rect(GameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            # length and rectangle
            plot_snake(GameWindow, black, snake_list, snake_size)
        pygame.display.update()            # this is important

        clock.tick(fps)          # find frame  in seconds



    pygame.quit()
    quit()

game_loop()