import random
import pygame
from game import game

def main():
    """
    In Processing, this is where void setup() would be #
    """
    size = (800, 800)

    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    game_field = game(size)

    """
    Main game loop which will be executed every frame below
    In Processing, this is where void draw() would be
    """
    while True:
        # Check for pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the screen is closed, quit the program
                pygame.quit()

        # This draws canvas and elipse
        screen.fill((0, 0, 0))
        game_field.update(pygame)
        game_field.display(pygame, screen)

        # updates the entire canvas
        pygame.display.flip()
        # limits the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()