import pygame


class Game:
    def __init__(self):
        self.running = True
        self.display = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Run to Roma") 
        self.clock = pygame.time.Clock()
        self.fps = 60
        # load app logo ./assets/runner-logo.png
        self.logo = pygame.image.load("./assets/runner-logo.png")
    
    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
    def update(self):
        pass

    def draw(self):
        pygame.display.set_icon(self.logo)
        self.display.fill((0, 0, 0))
        pygame.display.update()



if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
    quit()