import pygame as pg
import Specs as sp


class Wall(pg.sprite.Sprite):
    def __init__(self, display, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.display = display
        self.rect = pg.Rect(x, y, self.w, self.h)
        self.image = pg.Surface(self.rect.size)
        self.image.fill(sp.BLACK)

