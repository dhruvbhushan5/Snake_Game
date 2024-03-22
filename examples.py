import pygame
x = pygame.init()
# print(x)

# Creating Display for the game

game_window = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")

# Game specific variables

exit_game = False
quit_game = False

# Game LOOP

while not exit_game:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit_game = True
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                print("You pressed right arrow key")

pygame.quit()
quit()
