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

    def display(self, pygame, screen):
        pygame.draw.ellipse(screen, self.color, (self.x - self.radius, self.y - self.radius,  self.radius * 2, self.radius * 2))