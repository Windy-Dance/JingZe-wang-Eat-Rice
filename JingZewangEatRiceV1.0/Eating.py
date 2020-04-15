# coding : utf-8
import sys
import pygame
import random
lists = []
for i in range(100):
    tmp = (i+1)*10
    lists.append(tmp)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("yummy.mp3")
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("王境泽吃炒饭")
font = pygame.font.SysFont("SimHei", 50)


class WJZ:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.image = pygame.image.load("wjz.png").convert_alpha()
        self.speed = 4
        self.lmove = False
        self.rmove = False
        self.umove = False
        self.dmove = False

    def move(self):
        if self.lmove:
            self.x -= self.speed
            if self.x < 0:
                self.x = 1
        if self.rmove:
            self.x += self.speed
            if self.x > 660:
                self.x = 659
        if self.umove:
            self.y -= self.speed
            if self.y < 0:
                self.y = 1
        if self.dmove:
            self.y += self.speed
            if self.y > 660:
                self.y = 659


class CF:
    def restart(self):
        pygame.mixer.music.play(1,0)
        self.x = random.randint(0, self.mx)
        self.y = random.randint(0, self.my)

    def __init__(self):
        self.mx = 650
        self.my = 650
        self.x = random.randint(0, self.mx)
        self.y = random.randint(0, self.my)
        self.image = pygame.image.load("cf.png").convert_alpha()


def checkCrash(c, w):
    if (w.x + 0.7 * w.image.get_width() > c.x) and (
            w.x + 0.3 * w.image.get_width() < c.x + c.image.get_width()) and (
            w.y + 0.7 * w.image.get_height() > c.y) and (
            w.y + 0.3 * w.image.get_height() < c.y + c.image.get_height()):
        return True
    return False


wjz = WJZ()
cf = CF()
score = 0

cfm = []
for i in range(3):
    cfm.append(CF())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                wjz.lmove = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                wjz.rmove = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                wjz.dmove = True
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                wjz.umove = True
        if event.type == pygame.KEYUP:
            wjz.umove = False
            wjz.dmove = False
            wjz.rmove = False
            wjz.lmove = False
    screen.fill((230, 230, 230))
    fonts = font.render(f"分数:{score}",1,(255,255,255))
    
    if score > 0:
        if score in lists:
            for i in range(3):
                cfm.append(CF())
            del lists[0]
    for cfs in cfm:
        screen.blit(cfs.image,(cfs.x,cfs.y))
        if checkCrash(cfs,wjz):
            score += 1
            cfs.restart()
    wjz.move()
    screen.blit(wjz.image, (wjz.x, wjz.y))
    screen.blit(fonts,(0,0))
    pygame.display.update()
