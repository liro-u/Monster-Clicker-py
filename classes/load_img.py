import pygame


def load_img(a, pos, surface):
    img = pygame.image.load(a).convert_alpha()
    surface.blit(img, pos)
