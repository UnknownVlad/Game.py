import pygame

import fill
from Block import Block


class Magnet():

    def __init__(self, screen, gameField, data):
        self.data = data
        self.gameField = gameField
        self.screen = screen
        self.image = pygame.image.load('images/magnet2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def output(self):
        print(self.gameField.get_pos_block(self.rect.centerx // 100), len(self.gameField.listBlock))

        if(self.gameField.get_pos_block(self.rect.centerx // 100) + len(self.gameField.listBlock) >= 14):
            self.gameField.gameState = "over"
            return
        self.printDirection()
        self.printCatch()
        self.screen.blit(self.image, self.rect)


    def printDirection(self):
        pos = self.gameField.get_pos_block(self.rect.centerx // 100)

        for i in range(pos+1, self.gameField.row-1):
            k = Block(self.screen, 'images/course.png', self.rect.centerx-50, i*50)
            k.output()


    def printCatch(self):
        y = 700
        for i in self.gameField.listBlock:
            k = Block(self.screen, self.data.getImgBlocks()[i], self.rect.centerx-50, y-5)
            k.output()
            y-=50

    def update(self, x):
        if(x > self.checkBorderLeft() and x < self.checkBorderRight()):
            self.rect.centerx = x - x % 100 + 50

    def checkBorderLeft(self):
        size = len(self.gameField.listBlock)
        for j in range(self.rect.centerx // 100, -1, -1):
            p = self.gameField.get_pos_block(j)
            if(p + size+2 >= self.gameField.row):
                return (j+1)*100

        return 0

    def checkBorderRight(self):
        size = len(self.gameField.listBlock)
        for j in range(self.rect.centerx // 100, self.gameField.col):
            p = self.gameField.get_pos_block(j)
            if(p + size + 2 >= self.gameField.row):
                return j*100

        return 1100

    def click(self):
        self.gameField.update(self.rect.centerx // 100)

