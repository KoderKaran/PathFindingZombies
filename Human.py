import pygame as pg
import Images as im
import Specs as sp


class Human:
    def __init__(self, display, x, y):
        pg.sprite.Sprite.__init__(self)
        self.display = display
        self.idle_count = 0
        self.idle_img = im.HUMAN_IDLE
        self.x = x
        self.y = y

    def animate_idle(self):
        img = self.idle_img[self.idle_count // 2]
        self.idle_count += 1
        if self.idle_count >= 30:
            self.idle_count = 0
        return img