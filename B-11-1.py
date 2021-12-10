import pyxel
import random
import math

pyxel.init(200,200)

class Ball:
    speed = 3
    def __init__(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle) * Ball.speed
        self.vy = math.sin(angle) * Ball.speed

Var= [Ball(), Ball(), Ball()]
padx = 100
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
    global Var, padx, score, miss, balls, p, num1, num2, b
    for i in range(0, balls):
        if Var[i].x >= 200 or Var[i].x <= 0:
            Var[i].vx = -Var[i].vx
            num1 = random.randint(4,10)
            num2 = random.randint(1,15)
        Var[i].x += Var[i].vx
        Var[i].y += Var[i].vy
        if Var[i].y >= 200:
            pyxel.play(0, 1)
            Var[i].x = random.randint(0, 199)
            Var[i].y = 0
            angle = math.radians(random.randint(30,150))
            Var[i].x = math.cos(angle) * Ball.speed
            Var[i].y = math.sin(angle) * Ball.speed
            Var[i] = Ball()
            miss += 1
            num1 = random.randint(0, 10)
            num2 = random.randint(1,15)
        padx = pyxel.mouse_x
        if Var[i].y >= 195 and padx-20 <= Var[i].x <= padx+20:
            pyxel.play(0, 0)
            score += 10
            Var[i] = Ball()
            Ball.speed += 0.2
            Var[i].x = random.randint(0, 199)
            Var[i].y = 0
            angle =math.radians(random.randint(30,150))
            Var[i].vx = math.cos(angle) * Ball.speed
            Var[i].vy = math.sin(angle) * Ball.speed
            p += 1
            num1 = random.randint(4,10)
            num2 = random.randint(1,15)
            if p == 10 and balls < 3:
                balls += 1
                Ball.speed -= 2
                p = 0



def draw():
    global Var, padx, score, miss, balls, p, num1, num2, b
    if miss >= 10:
        pyxel.text(80, 90, "GAME OVER", 7)
        pyxel.stop()
    else:
        pyxel.cls(num2 - 1)
        for i in range(0, balls):
            pyxel.circ(Var[i].x, Var[i].y, num1, num2)
        pyxel.rect(padx-20, 195, 40, 5, 15)
        pyxel.text(10, 10, "score: " + str(score), 7)



pyxel.run(update, draw)
