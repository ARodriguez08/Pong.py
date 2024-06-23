import pygame

class Score:
    def __init__(self, font_size, window_width, window_height):
        self.player1_score = 0
        self.player2_score = 0
        self.font = pygame.font.Font(None, font_size)
        self.window_width = window_width
        self.window_height = window_height

    def increase_player1(self):
        self.player1_score += 1

    def increase_player2(self):
        self.player2_score += 1

    def draw(self, screen):
        player1_text = self.font.render(f"Player 1: {self.player1_score}", True, (255, 255, 255))
        player2_text = self.font.render(f"Player 2: {self.player2_score}", True, (255, 255, 255))
        
        player1_rect = player1_text.get_rect(topleft=(10, 10))
        player2_rect = player2_text.get_rect(topright=(self.window_width - 10, 10))
        
        screen.blit(player1_text, player1_rect)
        screen.blit(player2_text, player2_rect)
