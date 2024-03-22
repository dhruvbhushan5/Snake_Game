import pygame
import random

pygame.init()

# Screen Size
width = 900
height = 600

gameWindow = pygame.display.set_mode((width,height))
pygame.display.update()

# Game Title
pygame.display.set_caption("My First Game: SnakeswithDiptanshu")
# Defining Colors

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)

# Giving Background color
gameWindow.fill(white)
pygame.display.update()




font = pygame.font.SysFont(None,55)
clock = pygame.time.Clock()

# Score on screen function
def text_screen(text, color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color,[x, y, snake_size, snake_size])



# Game Loop
def gameloop():
    # Game Variables

    exit_game = False
    game_over = False

    snake_x = 50
    snake_y = 100
    velocity_x = 0
    velocity_y = 0
    init_velocity = 10
    snake_size = 20
    food_x = random.randint(0, width - snake_size)
    food_y = random.randint(0, height - snake_size)
    score = 0
    fps = 30

    snk_list = []
    snk_length = 1

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = init_velocity
                    velocity_y = 0
                if event.key == pygame.K_LEFT:
                    velocity_x = -init_velocity
                    velocity_y = 0
                if event.key == pygame.K_UP:
                    velocity_y = -init_velocity
                    velocity_x = 0
                if event.key == pygame.K_DOWN:
                    velocity_y = init_velocity
                    velocity_x = 0

        snake_x += velocity_x
        snake_y += velocity_y

        # Check if snake has collided with food
        if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:
            score += 10
            food_x = random.randint(0, width - snake_size)
            food_y = random.randint(0, height - snake_size)
            snk_length = snk_length + 5

        gameWindow.fill(white)

        text_screen("Score"+ str(score),blue,5,5)

        head=[]
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list)> snk_length:
            del snk_list[0]

        pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
        # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
        plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()