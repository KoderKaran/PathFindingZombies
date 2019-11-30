import pygame as pg
import Images as im
import Specs as sp


class Zombie(pg.sprite.Sprite):
    def __init__(self, display, x, y):
        pg.sprite.Sprite.__init__(self)
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
        if self.idle_count>= 30:
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

    def astar(self, other_x, other_y):
        if self.x < other_x:
            direction = False
        else:
            direction = True
        list = [(self.x+self.move_speed, self.y), (self.x-self.move_speed, self.y),
                (self.x, self.y+self.move_speed), (self.x, self.y-self.move_speed)]
        lowest_f = 10000000
        lowest_point = None
        for point in list:
            h_value = abs(point[0] - other_x) + abs(point[1] - other_y)
            f_value = h_value + self.g_value
            print(point)
            if f_value < lowest_f:
                lowest_f = f_value
                lowest_point = (point[0], point[1])
        pg.draw.line(self.display, sp.GREEN, (self.x, self.y), lowest_point)
        self.x = lowest_point[0]
        self.y = lowest_point[1]
        self.sequence.append(lowest_point)
        self.g_value+=self.move_speed
        if len(self.sequence) > 2 and self.x!=other_x and self.y!=other_y:
            self.walk(False, direction)
        elif self.x == other_x and self.y == other_y:
            print(self.sequence)
            self.g_value = 0
            self.walk(True, direction)

    def walk(self, found, direction):
        if not found:
            self.display.blit(pg.transform.flip(self.animate_walk(), direction, False), (self.x, self.y))
        else:
            self.display.blit(self.animate_idle(), (self.x, self.y))


    # def astar(self, other_x, other_y):
    #     open_points = []
    #     close_points = []
    #     curr_x, curr_y = self.x, self.y
    #     open_points.append((curr_x, curr_y))
    #     close_points.append((curr_x, curr_y))
    #     heuristic = abs(curr_x-other_x) + abs(curr_y-other_y)
    #     g_value = 0
    #     f_value = heuristic + g_value
    #     while curr_x != other_x and curr_y != other_y:
    #         adjacent = [(curr_x+self.move_speed, curr_y), (curr_x-self.move_speed, curr_y),
    #                     (curr_x, curr_y+self.move_speed), (curr_x, curr_y-self.move_speed)]
    #         for point in adjacent:
    #             print(point)
    #             if point not in close_points and point not in open_points:
    #                 open_points.append(point)
    #                 g_this = g_value + self.move_speed
    #                 h_this = abs(point[0]-other_x) + abs(point[1]-other_y)
    #                 f_this = g_this + h_this
    #                 if f_this < f_value:
    #                     f_value = f_this
    #                     curr_x, curr_y = point[0], point[1]
    #             close_points.append((curr_x, curr_y))
    #             g_value += self.move_speed
    #     print(open_points)
    #     for index, p in enumerate(close_points):
    #         print(index,p)
    #         try:
    #             pg.draw.line(self.display, sp.GREEN, p, close_points[index+1])
    #         except IndexError:
    #             pass