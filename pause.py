import pygame

class PauseMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.main_menu_items = ["Play", "Dificultad", "Acerca de", "Salir"]
        self.difficulty_menu_items = ["Facil", "Normal", "Dificil", "Regresar"]
        self.selected_item = 0
        self.font = pygame.font.Font(None, 36)
        self.current_menu = "main"  # To track which menu is currently displayed

    def reset_menu(self):
        self.selected_item = 0
        self.current_menu = "main"

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_item = (self.selected_item - 1) % len(self.get_current_menu_items())
            elif event.key == pygame.K_DOWN:
                self.selected_item = (self.selected_item + 1) % len(self.get_current_menu_items())
            elif event.key == pygame.K_RETURN:
                return self.select_menu_item()

        return None

    def get_current_menu_items(self):
        if self.current_menu == "main":
            return self.main_menu_items
        elif self.current_menu == "difficulty":
            return self.difficulty_menu_items
        elif self.current_menu == "about":
            return ["Regresar"]

    def select_menu_item(self):
        if self.current_menu == "main":
            selected_option = self.main_menu_items[self.selected_item]
            if selected_option == "Dificultad":
                self.current_menu = "difficulty"
                self.selected_item = 0
            elif selected_option == "Acerca de":
                self.current_menu = "about"
                self.selected_item = 0
            else:
                return selected_option
        elif self.current_menu == "difficulty":
            selected_difficulty = self.difficulty_menu_items[self.selected_item]
            if selected_difficulty == "Regresar":
                self.current_menu = "main"
                self.selected_item = 0
            else:
                return selected_difficulty
        elif self.current_menu == "about":
            self.current_menu = "main"
            self.selected_item = 0

    def draw(self, screen):
        if self.current_menu == "about":
            about_texts = ["Version: 1.0", "Creador: EDWIN ANTONIO RODRIGUEZ CRISANTOS"]
            y = self.height // 2 - len(about_texts) * 20
            for line in about_texts:
                text = self.font.render(line, True, (255, 255, 255))
                rect = text.get_rect(center=(self.width // 2, y))
                screen.blit(text, rect)
                y += 40
        else:
            for index, item in enumerate(self.get_current_menu_items()):
                color = (255, 255, 255) if index == self.selected_item else (100, 100, 100)
                text = self.font.render(item, True, color)
                rect = text.get_rect(center=(self.width // 2, self.height // 2 + index * 40))
                screen.blit(text, rect)
