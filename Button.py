import pygame

class Button():
    def __init__(self, screen, text, x, y, width, height, color_light = (170, 170, 170), color_dark = (100, 100, 100), font = 'Corbel', font_size = 35, font_color=(255, 255, 255)):
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        self.text = text
        self.screen = screen
        self.font_color = font_color
        self.font_size = font_size
        self.font = font
        self.color_dark = color_dark
        self.color_light = color_light

    def output(self, cX=-1, cY=-1):
        if self.checking_boundaries(cX, cY):
            pygame.draw.rect(self.screen, self.color_light, [self.x, self.y, self.width, self.height])
        else:
            pygame.draw.rect(self.screen, self.color_dark, [self.x, self.y, self.width, self.height])

        self.screen.blit(pygame.font.SysFont(self.font, self.font_size).render(self.text, True, self.font_color), (self.x + self.width//7, self.y))

    def checking_boundaries(self, cX, cY):
        if self.x <= cX <= self.x + self.width and self.y <= cY <= self.y + self.height:
            return True
        return False


