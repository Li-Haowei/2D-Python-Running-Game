import pygame

class Player:
    def __init__(self, game):
        self.movement = pygame.Vector2(0, 0)
        self.game = game
        self.image = self.game.load_img("assets/images/runner-logo.png")