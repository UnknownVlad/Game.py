import pygame

class Block():

    def __init__(self, screen, name_file, x, y):
        self.screen = screen
        self.image = pygame.image.load(name_file)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = x
        self.rect.y = y

    def output(self):
        self.screen.blit(self.image, self.rect)

