import pygame
from player import Player


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.title = "Haowei's Game"
        pygame.display.set_caption(self.title)
        self.player = Player()
    
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
            self.draw_player()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        self.player.update()
        # print(self.player.rect.x, self.player.rect.y)

    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.display.update()
    
    def quit(self):
        pygame.quit()
        quit()

    # show player on screen
    def draw_player(self):
        self.player.draw(self.screen)

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    game.quit()
