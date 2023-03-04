import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill("grey")

        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    game = Game()

    while True:
        game.run()