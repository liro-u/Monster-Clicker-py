import pygame
from pygame.locals import *


class Bouton:

    def __init__(self, color, x, y, width, height, text, fontsize, police, col, image=None):
        self.color = color
        self.x = x
        self.y = y
        self.text = text
        self.fontsize = fontsize
        self.police = police
        self.col = col

        if image:
            self.image = pygame.image.load(image).convert()
            self.width = self.image.get_width()
            self.height = self.image.get_height()
        else:
            self.width = width
            self.height = height
            self.image = None

    def draw(self, surface, outline):

        if self.image:
            surface.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(surface, outline, (self.x, self.y, self.width, self.height), 2)

        if self.text != '':
            ft = pygame.font.Font(self.police, self.fontsize)
            text = ft.render(self.text, True, self.col)
            surface.blit(text, (
                self.x + ((self.width - text.get_width()) / 2), self.y + ((self.height - text.get_height()) / 2 + 2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        else:
            return False

    """
    cette classe permet de parametrer un bouton
    il faut y entrer:
                color,
                x,
                y,
                width,
                height,
                text,
                fontsize,
                police,
                col         #couleur de la police
                
    pour le l'afficher il faut entrer :
                draw(
                    surface,
                    outline        #couleur du contour
                    )

    pour detecter la zone de clic il faut entrer:
                isOver(
                    pos
                    )
    """
