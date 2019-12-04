import pygame as pg
import Images as im
import Specs as sp


class Zombie(pg.sprite.Sprite):
    def __init__(self, display, x, y):
        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(x, y, 70, 100)
        # self.image = pg.Surface(self.rect.size).convert()
        # self.image.fill((255, 0, 0))
        self.display = display
        self.walk_count = 0
        self.idle_count = 0
        self.move_speed = 1
        self.idle_img = im.ZOMBIE_IDLE
        self.walk_img = im.ZOMBIE_WALK
        self.x = x
        self.y = y

    def animate_walk(self):
        img = self.walk_img[self.walk_count].convert_alpha()
        self.walk_count += 1
        if self.walk_count >= 10:
            self.walk_count = 0
        return img

    def animate_idle(self):
        img = self.idle_img[self.idle_count//2]
        self.idle_count += 1
        if self.idle_count >= 28:
            self.idle_count = 0
        return img

    def move(self):
        pass


class AStarZombie(Zombie):
    def __init__(self, display, x, y):
        pg.sprite.Sprite.__init__(self)
        Zombie.__init__(self, display, x, y)
        self.sequence = []
        self.g_value = 0
        self.last_dir = None

    def astar(self, other_x, other_y):
        if self.x < other_x:
            direction = False
            self.last_dir = False
        else:
            direction = True
            self.last_dir = True
        list = [(self.x+self.move_speed, self.y), (self.x-self.move_speed, self.y),
                (self.x, self.y+self.move_speed), (self.x, self.y-self.move_speed)]
        lowest_f = 10000000
        lowest_point = None
        for point in list:
            h_value = max(abs(point[0] - other_x), abs(point[1] - other_y))
            f_value = h_value + self.g_value
            if f_value < lowest_f:
                lowest_f = f_value
                lowest_point = (point[0], point[1])
        self.x = lowest_point[0]
        self.y = lowest_point[1]
        self.sequence.append(lowest_point)
        self.g_value+=self.move_speed
        try:
            tup_pos = (self.x, self.y)
            tup_other = (other_x, other_y)
            if tup_pos != tup_other:
                self.walk(False, direction)
            else:
                self.g_value = 0
                self.walk(True, self.last_dir)
        except:
            pass

    def walk(self, found, direction):
        try:
            for index, value in enumerate(self.sequence):
                pg.draw.line(self.display, sp.BLACK, self.sequence[index], self.sequence[index+1])
        except IndexError:
            pass
        if not found:
            self.display.blit(pg.transform.flip(self.animate_walk(), direction, False), (self.x, self.y))
        else:
            self.display.blit(pg.transform.flip(self.animate_idle(), direction, False), (self.x, self.y))
