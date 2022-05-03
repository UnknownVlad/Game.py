import pygame
import time

class Timer():
    def __init__(self, screen, x, y, width, height, time_start, text = "", color = (100, 100, 100), font = 'Corbel', font_size = 35, font_color=(255, 255, 255), plus = -1):
        self.time_start = time_start
        self.plus = plus
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        self.screen = screen
        self.font_color = font_color
        self.font_size = font_size
        self.font = font
        self.color = color
        self.time = time.clock()
        self.t = time_start
        self.text = text

    def output(self):
        if (time.clock() - self.time) > 1:
            self.time = time.clock()
            self.t+=self.plus
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height])
        self.screen.blit(pygame.font.SysFont(self.font, self.font_size).render(self.text+str(self.t), True, self.font_color), (self.x + 10, self.y))

    def set_timer(self):
        self.t = self.time_start
    #def output(self, t):
      # pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height])
     #   self.screen.blit(pygame.font.SysFont(self.font, self.font_size).render(self.text+str(t), True, self.font_color), (self.x + self.width//3.5, self.y))