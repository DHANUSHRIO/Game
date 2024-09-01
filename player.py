import pygame

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = 50
        self.height = 50
        self.speed = 5
        self.avatar = pygame.Surface((self.width, self.height))
        self.avatar.fill((255, 0, 0))
        self.rect = self.avatar.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.avatar, (self.x, self.y))

    def reset(self):
        self.x = 100
        self.y = 100
