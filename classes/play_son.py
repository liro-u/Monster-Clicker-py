import pygame


def play_son(son):
    a = pygame.mixer.Sound(son)
    a.play()
