from ball import ball
from paddle import paddle

class game:
    size = (0,0 )
    box_margin = 50
    b = ball(100, 100, 1, 3)
    p1 = paddle(100, 100)

    def __init__(self, screen_size):
        # Set own size to a smaller rectangle than the screen size
        self.size = (screen_size[0] - (self.box_margin * 2), screen_size[1] - (self.box_margin * 2))

    def update(self):
        self.b.update(self.box_margin, self.size[1] + self.box_margin)

    def display(self, pygame, screen):
        pygame.draw.lines(screen, (255, 255, 255), True,
                          [(self.box_margin, self.box_margin),
                           (self.box_margin, self.size[1] + self.box_margin),
                           (self.size[0] + self.box_margin, self.size[1] + self.box_margin),
                           (self.size[0] + self.box_margin, self.box_margin)], 2)

        self.b.display(pygame, screen)
        self.p1.display(pygame, screen)