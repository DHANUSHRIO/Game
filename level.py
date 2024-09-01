import pygame

class Level:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 800
        self.height = 600
        self.background = pygame.Surface((self.width, self.height))
        self.background.fill((0, 255, 0))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background, (self.x, self.y))
