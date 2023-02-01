"""
Player class will be used in the game to control the player.
And the look of the player.
"""

import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load("./assets/runner-logo.png")
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 10
        self.movement = pygame.Vector2(0, 0)
        self.time = 0
        self.time_count = 1
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.movement.x = 1
        if keys[pygame.K_LEFT]:
            self.movement.x = -1
        if keys[pygame.K_UP]:
            self.movement.y = -1
        if keys[pygame.K_DOWN]:
            self.movement.y = 1

    def stop(self):
        self.movement.x = 0
        self.movement.y = 0
    
    def move(self):
        self.rect.x += self.movement.x
        self.rect.y += self.movement.y

    def update(self):
        self.control()
        self.move()
        self.stop()
        