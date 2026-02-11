import pygame

class ball:
    radius = 7
    x = 0
    y = 0
    dx = 0
    dy = 0
    color = (255, 255, 255)

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def update(self, min_h, max_h):
        self.x += self.dx
        self.y += self.dy

        if self.y <= min_h + self.radius:
            self.dy *= -1
        if self.y >= max_h - self.radius:
            self.dy *= -1

        if self.x <= 50 + self.radius or self.x >= 750 - self.radius:
            self.x = self.y = 400
            return True

        return False

    def check_collide(self, paddle):
        paddle_rect = paddle.get_rect()
        if pygame.Rect.colliderect(paddle_rect, pygame.Rect(self.x - self.radius, self.y - self.radius,  self.radius * 2, self.radius * 2)):
            self.dx *= -1

    def display(self, pygame, screen):
        pygame.draw.ellipse(screen, self.color, (self.x - self.radius, self.y - self.radius,  self.radius * 2, self.radius * 2))