import pygame as pg
import Specs as sp
import Images as im
import Zombie as zm
import Human as hm
import random as ra
import Wall as w

pg.init()
display = pg.display.set_mode((sp.WIDTH, sp.HEIGHT), pg.RESIZABLE | pg.DOUBLEBUF)
pg.display.set_caption("Path Finding Simulator")

clock = pg.time.Clock()

running = True

zombies = pg.sprite.Group()
humans = pg.sprite.Group()
walls = pg.sprite.Group()

zombie = zm.AStarZombie(display, 100, 0)
des_x, des_y = ra.randint(0, sp.WIDTH-50), ra.randint(0, sp.HEIGHT-50)
human = hm.Human(display, des_x, des_y)

zombies.add(zombie)
humans.add(human)
first_bound = 0
size = 0


while running:
    display.fill(sp.WHITE)
    display.blit(human.animate_idle(), (human.x, human.y))
    events = pg.event.get()
    keys = pg.key.get_pressed()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            first_bound = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            size = first_bound[0] - pos[0]
            if size<0:
                walls.add(w.Wall(display, pos[0] + size, pos[1], abs(size), 20))
            else:
                walls.add(w.Wall(display, pos[0] , pos[1], abs(size), 20))
            first_bound = 0
            size = 0

    for wall in walls:
        display.blit(wall.image, (wall.x, wall.y))

    if zombie.x == human.x and zombie.y == human.y:
        zombie.walk(True, False)
    else:
        zombie.astar(human.x, human.y)

    if keys[pg.K_LEFT]:
        human.x -= 10
    if keys[pg.K_RIGHT]:
        human.x += 10
    if keys[pg.K_UP]:
        human.y -= 10
    if keys[pg.K_DOWN]:
        human.y += 10

    for i in zombies:
        if i.rect.x < 0:
            i.x = 0
        if i.x > sp.WIDTH - 70:
            i.x = sp.WIDTH - 70
        if i.y < 0:
            i.y = 0
        if i.y > sp.HEIGHT - 100:
            i.y = sp.HEIGHT - 100
    for i in humans:
        if i.x < 0:
            i.x = 0
        if i.x > sp.WIDTH - 40:
            i.x = sp.WIDTH - 40
        if i.y < 0:
            i.y = 0
        if i.y > sp.HEIGHT - 100:
            i.y = sp.HEIGHT - 100

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