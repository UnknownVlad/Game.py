from datetime import time

import pygame, sys
import pyautogui
import time

from Magnet import Magnet


def events(magnet):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            magnet.update(x)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(event.button == 1):
                magnet.click()


