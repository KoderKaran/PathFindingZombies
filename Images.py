import pygame as pg
import os


def get_imgs(sprite_type,type):
    os.chdir("C:\\Users\\yugio\\PycharmProjects\\PathFindingZombies\\" + sprite_type + "\\" + type)
    list_of_imgs = []
    for i in os.listdir():
        list_of_imgs.append(pg.image.load(i))
    return list_of_imgs


HUMAN_IDLE = get_imgs("human_sprites", "Idle")
ZOMBIE_IDLE = get_imgs("zombie_sprites", "Idle")
ZOMBIE_ATTACK = get_imgs("zombie_sprites", "Attack")
ZOMBIE_WALK = get_imgs("zombie_sprites", "Walk")

