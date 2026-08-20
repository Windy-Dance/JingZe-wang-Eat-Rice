# coding : utf-8

import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


class CF:
    image = pygame.image.load("cf.png").convert_alpha()

    def __init__(self):
        self.mx = 870
        self.my = 870
        self.x = random.randint(0, self.mx)
        self.y = random.randint(0, self.my)
        self.xs = random.randint(1, 2) + random.random()
        self.ys = random.randint(1, 2) + random.random()


cfs = []
for i in range(789):
    cfs.append(CF())

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    screen.fill((230, 230, 230))
    for c in cfs:
        screen.blit(c.image, (c.x, c.y))
        c.x -= c.xs
        c.y -= c.ys
        if c.y > 770 or c.y < 0:
            c.ys = -c.ys
        if c.x > 770 or c.x < 0:
            c.xs = -c.xs

    pygame.display.update()