import pygame
import random
import time

import sys

sys.path.append("../")
from constants import *


class Plus:
    def __init__(self, value, pos, col, police):
        self.value = value
        self.pos = pos
        self.start = time.time()

        self.font = pygame.font.SysFont(police, 20)
        text = self.font.render(f'+{self.value}', 1, col)
        self.taille = text.get_width(), text.get_height()

        self.surface = pygame.Surface(self.taille)
        self.alpha = 255

        self.surface.fill((255, 0, 255))
        self.surface.set_colorkey((255, 0, 255))

        self.surface.blit(text, (0, 0))

    def show(self, surf):
        life = time.time() - self.start
        self.alpha = ((3 - life) / 3) * 255
        self.surface.set_alpha(self.alpha)
        scale = life * 0.8 / 3 + 0.5
        surface = pygame.transform.scale(self.surface, ((int(self.taille[0] * scale), int(self.taille[1] * scale))))
        surf.blit(surface, self.pos)


class Bot:
    def __init__(self, name, values, prices):
        self.val_argent = values[0]
        self.val_uranium = values[1]
        self.repeat = values[2]
        self.name = name
        self.mult = 0
        self.prices = prices

        self.last = time.time()

    def update(self):

        if self.mult:
            current_time = time.time()

            if current_time - self.last > self.repeat:
                self.last = current_time
                return (TAILLE_FEN[0] // 2, TAILLE_FEN[1] // 2), (
                self.val_argent * self.mult, self.val_uranium * self.mult)

        return


class Player:
    def __init__(self):
        self.argent = 0
        self.uranium = 0
        self.val_argent = 1
        self.val_uranium = 1
        self.mult = 0
        self.plus = []

        self.bots = []

    def show(self, surf, plus=True):

        for i in self.plus[::-1]:
            if i.alpha < 0:
                del i
            elif plus:
                i.show(surf)

        for bot in self.bots:
            update = bot.update()
            if update:
                self.addPlus(update[0], update[1], plus)

    def changeBot(self, index, modif):

        if modif == 0:
            self.bots[index].mult += 1
        elif modif == 1:
            self.bots[index].repeat *= 0.9
        self.bots[index].prices[modif] = int(self.bots[index].prices[modif] * 1.1)

    def addPlus(self, pos, values, y_barre=None, plus=True):

        if not values:
            values = self.val_argent, self.val_uranium
        values = values[0] * (1 + self.mult), values[1] * (1 + self.mult)

        self.argent += values[0]
        self.uranium += values[1]

        if plus:
            col_1 = (235, 157, 3)
            col_2 = (15, 255, 0)
            if y_barre:
                range_x = max(pos[0] - 100, 0), min(pos[0] + 100, TAILLE_FEN[0])
                range_y = max(pos[1] - 100, y_barre + 40), min(pos[1] + 100, TAILLE_FEN[1])
            else:
                range_x = pos[0] - 100, pos[0] + 100
                range_y = pos[1] - 100, pos[1] + 100
            self.plus.append(
                Plus(values[0], [random.randint(range_x[0], range_x[1]), random.randint(range_y[0], range_y[1])], col_1,
                     police))
            if values[1]:
                self.plus.append(
                    Plus(values[1], [random.randint(range_x[0], range_x[1]), random.randint(range_y[0], range_y[1])],
                         col_2,
                         police))

    def click(self, fen, pos, y_barre):

        if pos[1] > y_barre + 40:
            val_uranium = self.val_uranium if random.random() < 1 / 7 else 0
            self.addPlus(pos, (self.val_argent, val_uranium), y_barre)
