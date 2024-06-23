import pygame

class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self, window_width, window_height, paddle1, paddle2):
        self.x += self.speed_x
        self.y += self.speed_y

        # Check if the ball hits top or bottom of the window
        if self.y <= 0 or self.y >= window_height - self.radius:
            self.speed_y = -self.speed_y

        # Check if the ball hits paddles
        if self.x <= paddle1.x + paddle1.width and paddle1.y <= self.y <= paddle1.y + paddle1.height:
            self.speed_x = abs(self.speed_x)
        if self.x >= paddle2.x - self.radius and paddle2.y <= self.y <= paddle2.y + paddle2.height:
            self.speed_x = -abs(self.speed_x)

    def draw(self, window, color):
        pygame.draw.circle(window, color, (self.x, self.y), self.radius)

    def adjust_position(self, window_width, window_height):
        if self.x < 0 or self.x > window_width:
            self.x = window_width // 2
            self.y = window_height // 2
