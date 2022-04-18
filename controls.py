import pygame
from gun import *
import sys
from bullet import Bullet
from ino import Ino

def events(screen,gun,bullets):
    "обработка событий"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
        elif event.type == pygame.KEYUP:
            #вправа
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen,gun)
                bullets.add(new_bullet)

def update(bg_color, screen, gun, inos, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    """обновлять пули"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_army(screen, inos):
    """создания армии пришельцев"""

    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    for ino_number in range(number_ino_x):
        ino = Ino(screen)
        ino.x = ino_width + ino_width * ino_number
        ino.rect.x = ino.x
        inos.add(ino)

