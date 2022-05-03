import stat
from collections import deque

import private as private
import time
import random
import pygame

import typeBlocks
from Block import Block


class GameField():

    def __init__(self, screen):
        #self.speed = speed
        #self.timing = time.time()
        #self.typeBlock = typeBlock
        self.score = 0
        self.screen = screen
        self.listBlock = list()
        self.row = 16#строка
        self.col = 11#столбец
        self.matrix = [[(-1) for i in range(self.col)] for j in range(self.row)]

        for i in range(3):
            self.shift_down()
            self.add_new_line()

        self.gameState = "play"



    def shift_down(self):
        self.matrix = self.matrix[-1:] + self.matrix[:-1]

    def add_new_line(self):
        for j in range(self.col):
            self.matrix[0][j] = typeBlocks.getRndImg()

    def get_pos_block(self, j):
        for i in range(self.row - 1, -1, -1):
            tB = self.matrix[i][j]
            if(tB != -1):
                return i
        return -1

    def check(self, i, j, tB):
        return 0 <= i < self.row and 0 <= j < self.col and self.matrix[i][j] == tB

    def remove_blocks(self, j):
        l = r = -1
        i = self.get_pos_block(j)

        queue = list()
        queue.append((i, j))

        blocks = list()
        blocks.append((i, j))

        tB = self.matrix[i][j]
        self.matrix[i][j] = -1

        c = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while(len(queue) != 0):
            cont = list()
            for i, j in queue:
                for i_, j_ in c:
                    t_i, t_j = i + i_, j + j_
                    if(self.check(t_i, t_j, tB)):
                        if(l == r == -1):
                            l = r = t_j
                        if (l > t_j):
                            l = t_j
                        if (r < t_j):
                            r = t_j
                        cont.append((t_i, t_j))
                        blocks.append((t_i, t_j))
                        self.matrix[t_i][t_j] = -1
            queue = cont

        if(len(blocks) < 4):
            l = r = -1
            for i, j in blocks:
                self.matrix[i][j] = tB
        else:
            self.score+=len(blocks)*len(blocks)
        print("score = ",self.score)
        return l, r

    def update(self, j):
        if(len(self.listBlock) == 0):
            self.get_blocks(j)
        elif(self.listBlock[0]!=5):
            self.repos_block(j)
            self.aux()
            #pygame.time.delay(1)
            self.timer(0.05)
            l, r = self.remove_blocks(j)
            self.aux()
            lFB = self.get_feeding_blosks(l, r)
            self.aux()
            #pygame.time.delay(20)
            self.timer(0.05)
            self.repos_feeding_blocks(l, r, lFB)
        else:
            self.del_this_line(j)
            self.aux()

    def get_blocks(self, j):
        l = list()
        pos = self.get_pos_block(j)
        c = self.matrix[pos][j]

        if (c == 5):
            l.append(c)

            self.listBlock = l
            self.matrix[pos][j] = -1
            return

        for i in range(pos, -1, -1):
            tB = self.matrix[i][j]
            if (c == tB and tB != 5 and tB != 6):
                l.append(tB)
                self.matrix[i][j] = -1
            else:
                break

        self.listBlock = l

    def del_this_line(self, j):
        pos = self.get_pos_block(j)
        self.matrix[pos][j] = 5
        self.aux()
        self.score += (pos * 30)
        for i in range(0, pos + 1):
            self.matrix[i][j] = -1

        self.listBlock = list()

    def repos_block(self, j):
        size = len(self.listBlock)
        pos = self.get_pos_block(j)
        print(self.listBlock)
        '''
        if (len(self.listBlock) == 1 and self.listBlock[0] == 5):
            for i in range(self.row):
                self.matrix[i][j] = -1
            return -1, -1
            '''
        if(size == 0 or size + pos >= self.row - 1):
            return


        for i in range(size):
            self.matrix[pos+i + 1][j] = self.listBlock[i]

        self.listBlock = list()

    def aux(self):
        #self.screen.fill((47, 79, 79))
        self.output()
        pygame.display.flip()


    def get_feeding_blosks(self, l, r):
        lFB = deque()
        for j in range(l, r  + 1):
            cont = list()
            for i in range(self.row):
                if(self.matrix[i][j] != -1):
                    cont.append(self.matrix[i][j])
                    self.matrix[i][j] = -1
            lFB.append(cont)

        return lFB

    def repos_feeding_blocks(self, l, r, lFC):
        for j in range(l, r+1):
            cont = lFC.popleft()
            if(cont == None):
                continue
            for i in range(len(cont)):
                self.matrix[i][j] = cont[i]

    def timer(self, interval):
        timing = time.time()
        while (time.time() - timing < interval):
            continue

    def draw_new_line(self):
        for j in range(self.col):
            if(self.get_pos_block(j) == 15):
                self.gameState = "over"

        self.shift_down()
        self.add_new_line()

    def draw_matrix(self):
        for i in range(self.row):
            for j in range(self.col):
                a = self.matrix[i][j]
                if(a == -1):
                    continue
                b = Block(self.screen, typeBlocks.getImg(a), j * 100, i*50)
                b.output()


    def output(self):
        self.draw_matrix()




