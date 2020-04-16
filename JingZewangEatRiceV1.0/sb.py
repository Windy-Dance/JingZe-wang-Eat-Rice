# coding : utf-8

import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

class CF:
    def restart(self):
        self.x = random.randint(0, self.mx)
        self.y = random.randint(0, self.my)

    def __init__(self):
        self.mx = 870
        self.my = 870
        self.x = random.randint(0, self.mx)
        self.y = random.randint(0, self.my)
        self.xs = random.randint(1,2) + random.random()
        self.ys = random.randint(1,2) + random.random()
        self.image = pygame.image.load("cf.png").convert_alpha()

cf = CF()
l = []
for i in range(789):
    l.append(CF())

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    screen.fill((230, 230, 230))
    for cf in l:
        screen.blit(cf.image, (cf.x, cf.y))
        cf.x -= cf.xs
        cf.y -= cf.ys
        if cf.y > 770 or cf.y < 0:
            cf.ys = -cf.ys
        if cf.x > 770 or cf.x < 0:
            cf.xs = -cf.xs

    pygame.display.update()
