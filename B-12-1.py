import pyxel
import random
import math


pyxel.init(200,200)


class Ball:
    speed = 2
    def __init__(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle) * Ball.speed
        self.vy = math.sin(angle) * Ball.speed
    def move(self):
        if self.x >= 200 or self.x <= 0:
            self.vx = -self.vx
            num1 = random.randint(4,10)
            num2 = random.randint(1,15)
        self.x += self.vx * Ball.speed
        self.y += self.vy * Ball.speed
VB = [Ball(), Ball(), Ball()]

class Pad:
    def __init__(self):
        self.padx = 100
VP = Pad()
score = 0
miss = 0
balls = 1
p = 0
num1 = 10
num2 = 7
b = 0

pyxel.sound(0).set(note='c3e3g3c4c4', tone='s', volume='4', effect=('n' * 4 + 'f'), speed=7)
pyxel.sound(1).set(note='f3 b2 f2 b1  f1 f1 f1 f1',tone='p',volume=('4' * 4 + '4321'),effect=('n' * 7 + 'f'),speed=9,)

def update():
    global VB, VP, score, miss, balls, p, num1, num2, b
    for i in range(0, balls):
        VB[i].move()
        if VB[i].y >= 200:
            pyxel.play(0, 1)
            VB[i] = Ball()
            miss += 1
            num1 = random.randint(0, 10)
            num2 = random.randint(1,15)
        VP.padx = pyxel.mouse_x
        if VB[i].y >= 195 and VP.padx-20 <= VB[i].x <= VP.padx+20:
            pyxel.play(0, 0)
            score += 10
            VB[i] = Ball()
            p += 1
            num1 = random.randint(4,10)
            num2 = random.randint(1,15)
            if p == 10 and balls < 3:
                balls += 1
                p = 0



def draw():
    global VB, VP, score, miss, balls, p, num1, num2, b
    if miss >= 10:
        pyxel.text(80, 90, "GAME OVER", 7)
        pyxel.stop()
    else:
        pyxel.cls(num2 - 1)
        for i in range(0, balls):
            pyxel.circ(VB[i].x, VB[i].y, num1, num2)
        pyxel.rect(VP.padx-20, 195, 40, 5, 15)
        pyxel.text(10, 10, "score: " + str(score), 7)



pyxel.run(update, draw)
