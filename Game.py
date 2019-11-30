import pygame as pg
import Specs as sp
import Images as im
import Zombie as zm
import Human as hm
import random as ra

pg.init()
display = pg.display.set_mode((sp.WIDTH, sp.HEIGHT), pg.RESIZABLE | pg.DOUBLEBUF)
pg.display.set_caption("Path Finding Simulator")

clock = pg.time.Clock()

running = True

zombies = pg.sprite.Group()
humans = pg.sprite.Group()

zombie = zm.AStarZombie(display, 100, 0)

doit = True
des_x, des_y = ra.randint(0, sp.WIDTH-200), ra.randint(0, sp.HEIGHT-200)
count = 0
while running:
    display.fill(sp.WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if zombie.x == des_x and zombie.y == des_y:
        zombie.walk(True, False)
    else:
        zombie.astar(des_x, des_y)
        count += 1
        print(count)
    if count > 600:
        print("changed!")
        changex = ra.randint(-100, 100)
        changey = ra.randint(-100, 100)
        des_x += changex
        des_y += changey
        count = -1000000000
    keys = pg.key.get_pressed()
    pg.display.flip()
    clock.tick(sp.FPS)

    # if keys[pg.K_LEFT]:
    #     movement = True
    #     left = True
    #     display.blit(pg.transform.flip(zombie.animate_walk(), left, False), (0, 0))
    # if keys[pg.K_RIGHT]:
    #     movement = True
    #     left = False
    #     display.blit(pg.transform.flip(zombie.animate_walk(), left, False), (0, 0))
    # if not movement:
    #     display.blit(pg.transform.flip(zombie.animate_idle(), left, False), (0, 0))