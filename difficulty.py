class DifficultySettings:
    def __init__(self):
        self.difficulties = {
            "Facil": 40,
            "Normal": 60,
            "Dificil": 120
        }

    def get_difficulty_ticks(self, level):
        return self.difficulties.get(level, 60)  # Default to Normal if not found
