
import time
import controls
import pygame

import fill
from Data import Data
from GameField import GameField
from tkinter import *
from tkinter.ttk import Combobox

from Magnet import Magnet
from Text_bar import Text_bar
from Button import Button
from Timer import Timer

import time


bg_color = (47, 79, 79)

pygame.init()
size_start_window = (500, 500)
screen = pygame.display.set_mode(size_start_window)

txt = Text_bar(screen, 'Select a level', 20, 40, 140, 40, None)
bnt_lvl1 = Button(screen, '1', 50, 90, 45, 45)
bnt_lvl2 = Button(screen, '2', 100, 90, 45, 45)
bnt_lvl3 = Button(screen, '3', 150, 90, 45, 45)
bnt_lvl4 = Button(screen, '4', 200, 90, 45, 45)
btn_quit = Button(screen, 'quit', 1000, 700, 140, 40)



text_game_state = Text_bar(screen, "", 400, 400, 140, 40, None, 90)

def output_all(cX = -1, cY = -1):
    txt.output()
    bnt_lvl1.output(cX, cY)
    bnt_lvl2.output(cX, cY)
    bnt_lvl3.output(cX, cY)
    bnt_lvl4.output(cX, cY)
    btn_quit.output(cX, cY)
    text_game_state.output()
    txt.output()

def motion_listener(cX, cY):
    if btn_quit.checking_boundaries(cX, cY):
        pygame.quit()
    elif bnt_lvl1.checking_boundaries(cX, cY):
        run(20, 200)
    elif bnt_lvl2.checking_boundaries(cX, cY):
        run(15, 600)
    elif bnt_lvl3.checking_boundaries(cX, cY):
        run(11, 1000)
    elif bnt_lvl4.checking_boundaries(cX, cY):
        run(8, 2000)


def start_window():
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                motion_listener(mouse[0], mouse[1])

        screen.fill(bg_color)
        mouse = pygame.mouse.get_pos()
        output_all(mouse[0], mouse[1])
        pygame.display.update()


size_x = 1100
size_y = 800

pygame.init()
screen = pygame.display.set_mode((size_x + 200, size_y))
pygame.display.set_caption("GAME")

#btn_quit = Button(screen, 'quit', size_x+ 50, size_y-50, 140, 40)
time_to_new_line = Text_bar(screen, 'Time to new', size_x+ 2, 10, 200, 40)
tmp_score = Text_bar(screen, 'Score: 0', size_x + 2, 200, 140, 40, None)

def draw_line():
    pygame.draw.line(screen, (14, 45, 15),
                     [size_x, 0],
                     [size_x, size_y], 3)



def run(t, needing_score):

    data = Data(fill.fillImgs())

    gameField = GameField(screen)
    magnet = Magnet(screen, gameField, data)

    clock = pygame.time.Clock()
    #t = 10
    timer_new_line = Timer(screen, size_x + 2, 50, 200, 40, t, 'line: ')
    #needing_score = 500
    n_s = Text_bar(screen, 'need: ' + str(needing_score), size_x + 2, 250, 140, 40, None)

    while True:

        if(gameField.gameState == "over"):
            text_game_state.set_text("U R LOSE")

            return
        if(timer_new_line.t == 0):
            gameField.draw_new_line()
            timer_new_line.set_timer()
        if(gameField.score >= needing_score):
            text_game_state.set_text("U R WIN")

            #game_state("U r win")
            return

        #mouse = pygame.mouse.get_pos()
        tmp_score.set_text("Score: " + str(gameField.score))

        controls.events(magnet)
        screen.fill(bg_color)
        magnet.output()
        gameField.output()
        draw_line()
        n_s.output()

        #btn_quit.output(mouse[0], mouse[1])

        time_to_new_line.output()
        tmp_score.output()
        timer_new_line.output()
        pygame.display.flip()
        clock.tick(60)

'''
def game_state(text):
    pygame.init()
    size_start_window = (500, 500)
    screen = pygame.display.set_mode(size_start_window)
    text = Text_bar(screen, text, 30, 10, 200, 40)
    while True:
        screen.fill(bg_color)
        text.output()
        pygame.display.update()
'''