class paddle:
    x = 0
    y = 0

    w = 20
    h = 80
    color = (0, 255, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def display(self, pygame, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))