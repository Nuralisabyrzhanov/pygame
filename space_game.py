import pygame
import sys
import controls
from controls import *
from gun import Gun
from pygame.sprite import Group


def run():

    pygame.init()
    screen = pygame.display.set_mode((700,500))
    pygame.display.set_caption("cosmic game")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    ino = Group()
    controls.create_army(screen,inos)


    while True:
        controls.events(screen,gun,bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(bullets)

run()
