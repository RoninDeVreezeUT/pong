from ball import ball
from paddle import paddle


class game:
    size = (0,0 )
    box_margin = 50
    b = ball(400, 400, 4, 1)
    p1 = paddle(100, 100)
    p2 = paddle(700, 100)

    playing = False

    def __init__(self, screen_size):
        # Set own size to a smaller rectangle than the screen size
        self.size = (screen_size[0] - (self.box_margin * 2), screen_size[1] - (self.box_margin * 2))

    def update(self, pygame):
        self.b.check_collide(self.p1)
        self.b.check_collide(self.p2)
        if self.playing:
            if self.b.update(self.box_margin, self.size[1] + self.box_margin):
                print("Ball hit screen")
                self.playing = False

        keys = pygame.key.get_pressed()
        player_1_movement = 0
        player_2_movement = 0

        if keys[pygame.K_UP]:
            player_2_movement = -7
            self.playing = True
        if keys[pygame.K_DOWN]:
            player_2_movement = 7
            self.playing = True
        if keys[pygame.K_w]:
            self.playing = True
            player_1_movement = -7
        if keys[pygame.K_s]:
            self.playing = True
            player_1_movement = 7

        self.p1.update(player_1_movement, 0, self.size[1] - self.box_margin)
        self.p2.update(player_2_movement, 0, self.size[1]  - self.box_margin)

    def display(self, pygame, screen):
        # Draw rectangle around game
        pygame.draw.lines(screen, (255, 255, 255), True,
                          [(self.box_margin, self.box_margin),
                           (self.box_margin, self.size[1] + self.box_margin),
                           (self.size[0] + self.box_margin, self.size[1] + self.box_margin),
                           (self.size[0] + self.box_margin, self.box_margin)], 2)

        # Draw dashed line in the middle
        for y in range(self.box_margin + 10, self.size[1] + self.box_margin + 10, self.size[1]//20):
            pygame.draw.rect(screen, (255, 255, 255), (self.size[0] / 2 - 2 + self.box_margin, y, 4, self.size[1]//40))

        # Draw ball and players
        self.b.display(pygame, screen)
        self.p1.display(pygame, screen)
        self.p2.display(pygame, screen)