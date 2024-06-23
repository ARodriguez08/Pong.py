import pygame

class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def draw(self, window, color):
        pygame.draw.rect(window, color, (self.x, self.y, self.width, self.height))

    def adjust_position(self, window_height):
        if self.y < 0:
            self.y = 0
        elif self.y > window_height - self.height:
            self.y = window_height - self.height
