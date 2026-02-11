import pygame

class paddle:
    x = 0
    y = 0

    w = 20
    h = 80
    color = (0, 255, 0)
    box_margin = 50

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, dy, min_y, max_y):
        # Move the paddle
        self.y += dy

        # Check at the top of out of bounds
        if self.y < self.box_margin + (self.h / 2):
            self.y = self.box_margin + (self.h / 2) # Move back to the edge of the bounds

        # Check at the bottom of out of bounds
        if self.y > 800 - self.box_margin - (self.h / 2):
            self.y = 800 - self.box_margin - (self.h / 2) # Move back to the edge of the bounds

    def get_rect(self):
        return pygame.Rect(self.x - (self.w / 2), self.y - (self.h / 2), self.w, self.h)

    def display(self, pygame, screen):
        pygame.draw.rect(screen, self.color, (self.x - (self.w / 2), self.y - (self.h / 2), self.w, self.h))
