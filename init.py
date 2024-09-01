import pygame
from player import Player
from level import Level
from cyberthreat import CyberThreat
from powerup import PowerUp
from database import Database
from menu import Menu

class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.level = Level()
        self.cyberthreat = CyberThreat()
        self.powerup = PowerUp()
        self.database = Database()
        self.menu = Menu()
        self.score = 0
        self.lives = 3
        self.level_number = 1

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            self.player.update()
            self.level.update()
            self.cyberthreat.update()
            self.powerup.update()
            self.check_collisions()
            self.update_score()
            self.update_lives()
            self.update_level()
            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            self.level.draw(self.screen)
            self.cyberthreat.draw(self.screen)
            self.powerup.draw(self.screen)
            self.menu.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def check_collisions(self):
        if self.player.rect.colliderect(self.cyberthreat.rect):
            self.lives -= 1
            self.player.reset()
        elif self.player.rect.colliderect(self.powerup.rect):
            self.score += 100
            self.powerup.reset()

    def update_score(self):
        self.score += 1

    def update_lives(self):
        if self.lives <= 0:
            self.game_over()

    def update_level(self):
        if self.score >= 1000:
            self.level_number += 1
            self.score = 0
            self.lives = 3

    def game_over(self):
        self.menu.game_over(self.score)
        self.database.insert_player("Player", self.score)
        self.score = 0
        self.lives = 3
        self.level_number = 1
