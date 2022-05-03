import pygame

class Text_bar():
    def __init__(self, screen, text, x, y, width, height, color = (100, 100, 100), font_size = 35, font = 'Corbel', font_color=(255, 255, 255)):
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        self.text = text
        self.screen = screen
        self.font_color = font_color
        self.font_size = font_size
        self.font = font
        self.color = color

    def output(self):
        if(self.color!=None):
            pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height])

        self.screen.blit(pygame.font.SysFont(self.font, self.font_size).render(self.text, True, self.font_color), (self.x + 10, self.y))

    def set_text(self, text):
        self.text = text